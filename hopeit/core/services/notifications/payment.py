from hopeit.core.services.notifications import Notification


class PaymentNotification(Notification):

    def __init__(self):
        self.data_message = {'type': self.TYPE_PAYMENT}

    def send_single_device(self, mobile_device_id, amount):
        self.push_service.notify_single_device(
            registration_id=mobile_device_id,
            message_body=str(amount),
            data_message=self.data_message,
            sound='Default')
