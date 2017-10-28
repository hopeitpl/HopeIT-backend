import chaps
import falcon
from falcon_cors import CORS

from hopeit.api.middlewares import SerializationMiddleware
from hopeit.api.resources import (
    goal, payment, device, message, user_message, stats)
from hopeit.api.resources.admin import user as admin_user
from hopeit.api.resources.admin import message as admin_message
from hopeit.api.resources.admin import (
    user_message as user_admin_message, user_payment as user_admin_payment,
    payment as admin_payment, dashboard)
from hopeit.api.resources.ping import Ping
from hopeit.app import configure_chaps
from hopeit.utils import RequestScope

cors = CORS(allow_all_origins=True, allow_all_headers=True,
            allow_all_methods=True)


class ScopedAPI(falcon.API):
    def __call__(self, env, start_response):
        with RequestScope.scope:
            try:
                resp = super().__call__(env, start_response)
            except Exception:
                chaps.Container().get_object('db_session').close(rollback=True)
                raise
            finally:
                chaps.Container().get_object('db_session').close()
        return resp


def configure_api(class_=ScopedAPI):
    configure_chaps()
    api = class_(middleware=[
        cors.middleware,
        SerializationMiddleware()
    ])

    api.add_route('/_ping', Ping())
    api.add_route('/users/{user_id}/goal', goal.Item())
    api.add_route('/users/{user_id}/device', device.Item())
    api.add_route('/users/{user_id}/stats', stats.Item())
    api.add_route('/payments', payment.CreatePayment())
    api.add_route('/payments/verify', payment.GetPaymentStatus())
    api.add_route('/payments/{user_id}', payment.Collection())
    api.add_route('/messages/user/{user_id}', user_message.Item())
    api.add_route('/messages/{message_id}', message.Item())

    # Admin urls
    api.add_route('/admin/users', admin_user.Collection())
    api.add_route('/admin/dashboard', dashboard.Item())
    api.add_route('/admin/users/{user_id}', admin_user.Item())
    api.add_route('/admin/messages', admin_message.Collection())
    api.add_route('/admin/messages/{message_id}', admin_message.Item())
    api.add_route('/admin/messages/user/{user_id}', user_admin_message.Item())
    api.add_route('/admin/payments', admin_payment.Collection())
    api.add_route('/admin/payments/user/{user_id}',
                  user_admin_payment.Collection())

    return api
