from chaps import inject

from hopeit.actions import Action
from hopeit.core.models import Goal, User


@inject('db_session')
class GetUserStatsAction(Action):
    def do(self):
        user = self.db_session.query(User).filter(
            User.id == self.payload['user_id']).first()
        return {
            'total_amount': int(sum(p.operation_amount for p in
                                    user.payments)),
            'total_payments': user.payments.count(),
            'finished_goals': user.goals.filter(Goal.finished.is_(
                True)).count()
        }
