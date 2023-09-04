from typing import Optional

from web3_utils import Web3

from actions.base import BaseAction
from web3_utils import (
    Transaction, TransactionConfig, TransactionExecutionType,
)
from web3_utils.transactions.utils import (
    calculate_random_transaction_value,
)
from web3_utils.types import TransactionReceipt
from web3_utils.utils import get_node_rpc_url

from .configs import StargateFinanceSwapConfig
from .utils import (
    get_stargate_router_contract,
    get_stargate_swap_method,
    get_stargate_swap_method_args
)


class StargateFinanceSwap(BaseAction):

    name = 'Stargate Swap'
    validator = StargateFinanceSwapConfig
    config: StargateFinanceSwapConfig

    def _perform_execution(self) -> Optional[TransactionReceipt]:
        self.config.tx.value = calculate_random_transaction_value(self.config.tx)
        self.config.amount_ld.calculate_random_value()
        if not (self.config.tx.value or self.config.amount_ld.value):
            return

        web3 = Web3(Web3.HTTPProvider(get_node_rpc_url(self.config.from_chain)))
        contract = get_stargate_router_contract(
            web3,
            self.config.from_chain,
            self.config.from_token
        )
        contract_method = get_stargate_swap_method(
            contract,
            self.config.from_token
        )
        method_args = get_stargate_swap_method_args(self.config)
        transaction_config = TransactionConfig(
            wallet=self.config.wallet,
            chain=self.config.from_chain,
            type=TransactionExecutionType.send,
            amount=self.config.tx.get_amount(),
            gas=self.config.tx.get_gas(),
            contract=contract.address,
            contract_method=contract_method,
            contract_method_args=method_args.to_list()
        )

        transaction = Transaction(transaction_config)
        receipt = transaction.send(wait=True)

        if transaction.config.hash:
            self.log('Transaction successfully sent.')
            self.log(transaction.config.hash.hex())
        else:
            self.log('Unable to send transaction.')

        return receipt
