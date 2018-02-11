import chaps

# noinspection PyUnresolvedReferences
from hopeit.core import models  # noqa
from hopeit.core.config import Config
from hopeit.core.services.notifications import fcm_factory
from hopeit.core.services.payments.dotpay import Dotpay
from hopeit.core.utils import REQUEST_SCOPE, RequestScope


@chaps.scope(chaps.SINGLETON_SCOPE)
class HopeIT(object):
    def run(self, action):
        result = action.do()
        return result


def configure_chaps():
    from hopeit.core.database import DbSessionMaker, DbSession

    chaps.Container.configure({
        'app': HopeIT,
        'db_session_maker': DbSessionMaker,
        'db_session': DbSession,
        'config': Config,
        'push_service': fcm_factory,
        'payments': Dotpay,
    })
    chaps.Container().register_scope(REQUEST_SCOPE, RequestScope)
