import chaps
import falcon
from falcon_cors import CORS

from hopeit.api.middlewares import SerializationMiddleware
from hopeit.api.resources import goal, payment
from hopeit.api.resources.admin import user as admin_user
from hopeit.api.resources.ping import Ping
from hopeit.app import configure_chaps
from hopeit.utils import RequestScope

cors = CORS(allow_all_origins=True, allow_all_headers=True,
            allow_all_methods=True)


class ScopedAPI(falcon.API):
    def __call__(self, env, start_response):
        with RequestScope.scope:
            resp = super().__call__(env, start_response)
            chaps.Container().get_object('db_session').close()
        return resp


def configure_api(class_=ScopedAPI):
    configure_chaps()
    api = class_(middleware=[
        cors.middleware,
        SerializationMiddleware()
    ])

    api.add_route('/_ping', Ping())
    api.add_route('/users/{user_id}/goals', goal.Item())
    api.add_route('/payment', payment.CreatePayment())
    api.add_route('/payment/verify', payment.GetPaymentStatus())

    # Admin urls
    api.add_route('/admin/users', admin_user.Collection())
    api.add_route('/admin/users/{user_id}', admin_user.Item())

    return api
