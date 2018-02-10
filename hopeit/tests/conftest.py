import chaps
import pytest
from alembic.command import upgrade as alembic_upgrade
from alembic.config import Config as AlembicConfig
from chaps.scope.thread import ThreadScope
from hopeit.core.app import HopeIT
from hopeit.core.config import Config
from hopeit.core.database import DbSession
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from hopeit.core.utils import REQUEST_SCOPE


@pytest.fixture()
def make_migrations():
    alembic_config = AlembicConfig('alembic.ini')
    alembic_config.set_main_option('script_location', 'alembic')
    alembic_upgrade(alembic_config, 'head')


@pytest.fixture(scope="function")
def db_session(make_migrations, request):
    app_cfg = chaps.Container().get_object('config')
    engine = create_engine(app_cfg.DATABASE_URL, poolclass=NullPool)
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection, autoflush=True)
    session = Session()
    session.begin(subtransactions=True)

    class DbTestSession(DbSession):
        def __init__(self):
            self._session = session

        @property
        def session(self):
            return session

        def __getattr__(self, item):
            return getattr(session, item)

    yield DbTestSession

    # Code below executes only when pytest goes out of scope.
    # Here - when test function ends.
    transaction.rollback()
    connection.close()


class _ClassCallMock(object):
    def __init__(self):
        self.calls = []

    def __getattr__(self, item):
        def f(*a, **kw):
            self.calls.append((item, a, kw))

        return f


@pytest.fixture()
def push_service_mock():
    return _ClassCallMock()


@pytest.fixture()
def push_service_mock_factory(push_service_mock):
    def f():
        return push_service_mock

    return f


@pytest.fixture()
def configure_chaps(db_session, push_service_mock_factory):
    chaps.Container._reset()

    chaps.Container.configure({
        'app': HopeIT,
        'db_session': db_session,
        'config': Config,
        'push_service': push_service_mock_factory,
        'payments': lambda x: None
    })
    chaps.Container().register_scope(REQUEST_SCOPE, ThreadScope)


@pytest.fixture()
def hopeit(configure_chaps):
    return HopeIT()
