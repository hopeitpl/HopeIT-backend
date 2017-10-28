from chaps import inject

from hopeit.actions import Action
from hopeit.models import Payment


@inject('db_session')
class GetUserPaymentsAction(Action):

    def get_user_payments(self, user_id):
        return self.db_session.query(Payment).filter(
            Payment.user_id == user_id)

    def do(self):
        return {'payments': [{
            'id': p.id,
            'user_id': p.user_id,
            'goal_id': p.goal_id,
            'operation_number': p.operation_number,
            'operation_type': p.operation_type,
            'operation_status': p.operation_status,
            'operation_amount': p.operation_amount,
            'operation_currency': p.operation_currency,
            'operation_datetime': str(p.operation_datetime),
            'channel': p.channel,
            'signature': p.signature
        } for p in self.get_user_payments(self.payload['user_id'])]}
