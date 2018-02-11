import chaps
import falcon
from falcon_cors import CORS

from hopeit.api.middlewares import SerializationMiddleware
from hopeit.api.resources import (device, goal, message, payment,
                                  send_payment_notify, stats, user_message)
from hopeit.api.resources.admin import dashboard
from hopeit.api.resources.admin import message as admin_message
from hopeit.api.resources.admin import payment as admin_payment
from hopeit.api.resources.admin import user as admin_user
from hopeit.api.resources.admin import user_message as user_admin_message
from hopeit.api.resources.admin import user_payment as user_admin_payment
from hopeit.api.resources.ping import Ping
from hopeit.core.utils import RequestScope

cors = CORS(allow_all_origins=True, allow_all_headers=True,
            allow_all_methods=True)


class ScopedAPI(falcon.API):
    def __call__(self, env, start_response):
        with RequestScope.scope:
            db_session = chaps.Container().get_object('db_session')
            try:
                resp = super().__call__(env, start_response)
            except Exception:
                db_session.close(rollback=True)
                raise
            finally:
                db_session.commit()
                db_session.close()
        return resp


def configure_api(class_=ScopedAPI):
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
    api.add_route('/notifications/send_payment/{user_id}',
                  send_payment_notify.Item())

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
