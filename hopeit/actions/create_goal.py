from datetime import datetime, timedelta

from hopeit.actions import Action
from hopeit.models import Goal


class CreateGoal(Action):
    def do(self):
        goal = Goal(
            user_id=self.payload['user_id'],
            amount=self.payload['amount'],
            finish_at=datetime.now() + timedelta(days=30 * self.payload(['months']))
        )