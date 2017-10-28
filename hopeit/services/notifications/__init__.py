import chaps

from chaps import scope, Inject, SINGLETON_SCOPE
from pyfcm import FCMNotification


@scope(SINGLETON_SCOPE)
def fcm_factory():
    config = chaps.Container().get_object('config')
    return FCMNotification(api_key=config.GOOGLE_API_KEY)


class Notification(object):

    TYPE_MESSAGE = 'message'
    TYPE_PAYMENT = 'payment'
    TYPE_PAYMENT_CONFIRM = 'payment_confirm'
    TYPE_GOAL_COMPLETED = 'goal_completed'

    push_service = Inject('push_service')

    def send_single_device(self, mobile_device_id):
        return NotImplemented

    def send_multiple_devices(self, mobile_device_ids):
        return NotImplemented
