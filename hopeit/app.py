import chaps

from hopeit.config import Config
from hopeit.utils import REQUEST_SCOPE, RequestScope

from hopeit.services.notifications import fcm_factory


@chaps.scope(chaps.SINGLETON_SCOPE)
class HopeIT(object):
    def run(self, action):
        try:
            result = action.do()
        except Exception:
            chaps.Container().get_object('db_session').close(rollback=True)
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
        'push_service': fcm_factory
    })
    chaps.Container().register_scope(REQUEST_SCOPE, RequestScope)
