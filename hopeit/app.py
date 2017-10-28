import chaps

# noinspection PyUnresolvedReferences
from hopeit import models  # noqa
from hopeit.config import Config
from hopeit.services.payments.dotpay import Dotpay
from hopeit.utils import REQUEST_SCOPE, RequestScope

from hopeit.services.notifications import fcm_factory


@chaps.scope(chaps.SINGLETON_SCOPE)
class HopeIT(object):
    def run(self, action):
        db_session = chaps.Container().get_object('db_session')
        try:
            result = action.do()
            db_session.close()
        except Exception:
            db_session.close(rollback=True)
            raise
        else:
            return result


def configure_chaps():
    from hopeit.database import DbSessionMaker, DbSession

    chaps.Container.configure({
        'app': HopeIT,
        'db_session_maker': DbSessionMaker,
        'db_session': DbSession,
        'config': Config,
        'push_service': fcm_factory,
        'payments': Dotpay,
    })
    chaps.Container().register_scope(REQUEST_SCOPE, RequestScope)
