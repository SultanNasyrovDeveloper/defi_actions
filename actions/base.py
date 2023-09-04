from web3_utils import Web3

from .planner.models import TaskExecution

from actions.configs import BaseActionConfig
from web3_utils import get_node_rpc_url


class BaseAction:

    name: str

    def __init__(self, config: BaseActionConfig, logger, execution, *args, **kwargs):
        self.config = config
        self.logger = logger
        self.execution: TaskExecution = execution
        self.bot = self.execution.task.bot
        self.wallet = self.bot.wallet

    def set_up(self):
        ...

    def tear_down(self):
        self.execution.save()

    def execute(self):
        self.log(f'Starting execution of {self.name} with {self.config.dict()}')
        self.set_up()
        self._perform_execution()
        self.tear_down()

    def log(self, message: str):
        """
        Logs message to execution.
        Execution logs are stored in database in a special field. This method does not save execution
        to database but just modifies current field value.
        """
        self.logger.info(message)
        self.execution.logs.append(message)

    def _perform_execution(self):
        """
        Implement execution logic here in child classes.
        """
        raise NotImplementedError
