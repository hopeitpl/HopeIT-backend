from hopeit.services.notifications import Notification

PUSH_NOTIFICATION_MESSAGE = 'test'


class PaymentNotificationConfirm(Notification):

    def __init__(self):
        self.data_message = {'type': self.TYPE_PAYMENT_CONFIRM}

    def send_single_device(self, mobile_device_id):
        self.push_service.notify_single_device(
            registration_id=mobile_device_id,
            message_body=PUSH_NOTIFICATION_MESSAGE,
            data_message=self.data_message,
            sound='Default')
