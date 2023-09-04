from web3_utils import Web3

from actions.base import BaseAction
from web3_utils.web3 import (
    Transaction, TransactionConfig, TransactionExecutionType,
)
from web3_utils.transactions.utils import (
    calculate_random_transaction_value,
)
from web3_utils.utils import get_node_rpc_url

from .abi import SWAP_ROUTER_ABI
from .configs import ArbSwapActionConfig, ArbswapMethodArgs
from .utils import get_router_address


class ArbSwapAction(BaseAction):

    name = 'Arbswap'
    validator = ArbSwapActionConfig
    config: ArbSwapActionConfig

    def _perform_execution(self):
        web3 = Web3(Web3.HTTPProvider(get_node_rpc_url(self.config.chain)))
        contract = web3.eth.contract(
            address=get_router_address(self.config.chain),
            abi=SWAP_ROUTER_ABI
        )
        self.config.amount.value = calculate_random_transaction_value(self.config.amount)
        self.log(f'Random value generated {web3.from_wei(self.config.amount.value, "ether")}')
        method_args = ArbswapMethodArgs.from_action_config(self.config)
        transaction_config = TransactionConfig(
            wallet=self.config.wallet,
            chain=self.config.chain,
            type=TransactionExecutionType.send,
            amount=self.config.amount.get_amount(),
            gas=self.config.amount.get_gas(),
            contract=get_router_address(self.config.chain),
            contract_method=contract.functions.swap,
            contract_method_args=method_args.to_list()
        )
        transaction = Transaction(transaction_config)
        receipt = transaction.send(wait=True)

        if transaction.config.hash:
            self.log('Transaction successfully sent')
            self.log(transaction.config.hash.hex())
