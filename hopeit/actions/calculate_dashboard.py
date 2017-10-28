from chaps import inject
from sqlalchemy import func

from hopeit.actions import Action
from hopeit.models import Payment, User, Goal


@inject('db_session')
class CalculateDashboardAction(Action):
    def do(self):
        return {
            'total_balance': self.db_session.query(
                func.sum(Payment.operation_amount)).scalar() or 0,
            'total_payments': self.db_session.query(
                Payment).count(),
            'total_users': self.db_session.query(User).count(),
            'total_goal': self.db_session.query(
                func.sum(Goal.target)).scalar() or 0
        }
