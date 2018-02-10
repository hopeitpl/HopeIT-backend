from hopeit.core.services.notifications import Notification

PUSH_NOTIFICATION_MESSAGE = 'Nowa wiadomość'


class MessageNotification(Notification):

    def __init__(self):
        self.data_message = {'type': self.TYPE_MESSAGE}

    def send_single_device(self, mobile_device_id):
        self.push_service.notify_single_device(
            registration_id=mobile_device_id,
            message_body=PUSH_NOTIFICATION_MESSAGE,
            data_message=self.data_message,
            sound='Default')

    def send_multiple_devices(self, mobile_device_ids):
        self.push_service.notify_multiple_devices(
            registration_ids=mobile_device_ids,
            message_body=PUSH_NOTIFICATION_MESSAGE,
            data_message=self.data_message,
            sound='Default')
