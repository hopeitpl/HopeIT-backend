from hopeit.services.notifications import Notification

PUSH_NOTIFICATION_MESSAGE = 'Cel został osiągnięty'


class GoalCompletedNotification(Notification):

    def __init__(self):
        self.data_message = {'type': self.TYPE_GOAL_COMPLETED}

    def send_single_device(self, mobile_device_id):
        self.push_service.notify_single_device(
            registration_id=mobile_device_id,
            message_body=PUSH_NOTIFICATION_MESSAGE,
            data_message=self.data_message,
            sound='Default')
