import chaps
import falcon

from hopeit.api.middlewares import SerializationMiddleware, ValidationMiddleware
from hopeit.api.resources import Resource
from hopeit.app import configure_chaps
from hopeit.utils import RequestScope
from hopeit.api.hooks.authorization import authorize_user


class ScopedAPI(falcon.API):
    def __call__(self, env, start_response):
        with RequestScope.scope:
            resp = super().__call__(env, start_response)
            chaps.Container().get_object('db_session').close()
        return resp


class Ping(Resource):

    @falcon.before(authorize_user)
    def on_get(self, req, resp):
        resp.payload = {'resp': 'PONG'}


def configure_api(class_=ScopedAPI):
    configure_chaps()
    api = class_(middleware=[
        SerializationMiddleware(),
        ValidationMiddleware()
    ])

    api.add_route('/_ping', Ping())

    return api
