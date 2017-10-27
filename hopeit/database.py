from chaps import SINGLETON_SCOPE, inject, scope, Inject
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from hopeit.utils import REQUEST_SCOPE

Base = declarative_base()


@scope(SINGLETON_SCOPE)
class DbSessionMaker(object):
    config = Inject('config')

    def __init__(self):
        self.engine = create_engine(self.config.DATABASE_URL)
        self.session_maker = sessionmaker(bind=self.engine)

    def __call__(self, *args, **kwargs):
        return self.session_maker(*args, **kwargs)


@scope(REQUEST_SCOPE)
class DbSession(object):
    @inject
    def __init__(self, db_session_maker):
        self._session = None

    @property
    def session(self):
        if not self._session:
            self._session = self.db_session_maker.session_maker()
        return self._session

    def close(self, rollback=False):
        if not self._session:
            return
        else:
            if rollback:
                self._session.rollback()
            else:
                self._session.commit()
            self._session.close()
            self._session = None

    def __getattr__(self, item):
        return getattr(self.session, item)

    def __del__(self):
        self.close()
