from datetime import datetime, timedelta

from chaps import inject

from hopeit.actions import Action
from hopeit.models import Goal


@inject('db_session')
class CreateGoalAction(Action):
    def do(self):
        goal = Goal(
            user_id=self.payload['user_id'],
            target=self.payload['target'],
            finish_at=datetime.now() + timedelta(
                days=30 * self.payload(['months']))
        )
        self.db_session.add(goal)
