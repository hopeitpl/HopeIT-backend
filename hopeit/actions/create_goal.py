from datetime import datetime, timedelta

from chaps import inject

from hopeit.actions import Action
from hopeit.models import Goal
from hopeit.models.goal import NotificationsFreq


@inject('db_session')
class CreateGoalAction(Action):
    def do(self):
        goal = self.db_session.query(Goal).filter(
            Goal.finished.is_(False),
            Goal.user_id == self.payload['user_id']).first()

        if goal is None:
            goal = Goal(
                user_id=self.payload['user_id'],
                target=self.payload['target'],
                finish_at=datetime.now() + timedelta(
                    days=30 * int(self.payload['months'])),
                notify_freq=NotificationsFreq(int(self.payload['notify_freq']))
            )
            self.db_session.add(goal)
