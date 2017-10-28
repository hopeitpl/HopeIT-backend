from chaps import inject
from hopeit.actions import Action
from hopeit.models import Payment


@inject('db_session')
class GetAllPaymentsAction(Action):

    def get_payments(self):
        return self.db_session.query(Payment).order_by(
            Payment.operation_datetime.desc())

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
        } for p in self.get_payments()]}
