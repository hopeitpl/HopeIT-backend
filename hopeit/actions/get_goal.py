from chaps import inject

from hopeit.actions import Action
from hopeit.models import Goal


@inject('db_session')
class GetGoalAction(Action):
    def do(self):
        goal = self.db_session.query(Goal).filter(
            Goal.finished.is_(False)).first()
        if goal:
            return {
                'target': goal.target,
                'balance': goal.balance,
                'next_notification': str(goal.next_notification)
            }
        else:
            return {
                'target': None,
                'balance': None,
                'next_notification': None
            }
