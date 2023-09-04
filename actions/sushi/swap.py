from actions.base import BaseAction

from .configs import SushiSwapConfig


class SushiSwapAction(BaseAction):

    name = 'Sushi Swap'

    validator = SushiSwapConfig

    def _perform_execution(self):
        self.log('Performing sushi swap action')


