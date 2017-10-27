import chaps
import falcon

from hopeit.api.middlewares import SerializationMiddleware
from hopeit.api.resources.ping import Ping
from hopeit.app import configure_chaps
from hopeit.utils import RequestScope


class ScopedAPI(falcon.API):
    def __call__(self, env, start_response):
        with RequestScope.scope:
            resp = super().__call__(env, start_response)
            chaps.Container().get_object('db_session').close()
        return resp


def configure_api(class_=ScopedAPI):
    configure_chaps()
    api = class_(middleware=[
        SerializationMiddleware()
    ])

    api.add_route('/_ping', Ping())

    return api
