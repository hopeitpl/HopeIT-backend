from hopeit.actions import Action


class PingAction(Action):
    def do(self):
        # self.payload <= dane z requesta

        return {
            'results': 'pong'
        }