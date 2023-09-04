from web3 import Web3

from web3_utils import (
    calculate_random_transaction_value,
    get_node_rpc_url,
    get_token_contract_address,
    ERC20_TOKEN_ABI
)
from web3_utils.transactions import TransactionConfig, Transaction

from ..base import BaseAction
from .configs import ApproveConfig


class ApproveAction(BaseAction):

    name = 'Approve'
    config: ApproveConfig
    validator = ApproveConfig

    def _perform_execution(self):
        web3 = Web3(Web3.HTTPProvider(get_node_rpc_url(self.config.chain)))
        self.config.amount.calculate_random_value()
        amount = self.config.amount.value
        self.config.amount.value = 0
        if web3.is_connected():
            address = get_token_contract_address(
                chain=self.config.chain,
                token=self.config.token
            )
            contract = web3.eth.contract(address=address, abi=ERC20_TOKEN_ABI)
            contract_method = contract.functions.approve
            transaction_config = TransactionConfig(
                wallet=self.config.wallet,
                chain=self.config.chain,
                contract=address,
                contract_method=contract_method,
                contract_method_args=[
                    self.config.spender,
                    amount
                ],
                amount=self.config.amount.get_amount(),
                gas=self.config.amount.get_gas()
            )
            transaction = Transaction(transaction_config)
            try:
                receipt = transaction.send(wait=True)
                self.log(receipt.transactionHash.hex())
            except Exception as e:
                self.log('Approve allowance action execution failed')
                self.log(str(e))
