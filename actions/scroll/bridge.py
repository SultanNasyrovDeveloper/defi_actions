from web3_utils import Web3

from web3_utils import (
    Transaction, TransactionConfig, TransactionExecutionType,
    get_node_rpc_url, EVMChain
)

from ..base import BaseAction
from . import abi, configs, constants


class ScrollBridge(BaseAction):

    name = 'Scroll Bridge'
    validator = configs.ScrollBridgeConfig
    config: configs.ScrollBridgeConfig

    def _perform_execution(self):
        web3 = Web3(Web3.HTTPProvider(get_node_rpc_url(EVMChain.goerli)))
        contract = web3.eth.contract(
            abi=abi.SCROLL_BRIDGE_ABI,
            address=constants.MAINNET_BRIDGE_CONTRACT_ADDRESS
        )
        self.config.tx.calculate_random_value()

        tx_config = TransactionConfig(
            wallet=self.config.wallet,
            chain=EVMChain.goerli,
            type=TransactionExecutionType.send,
            amount=self.config.tx.get_amount(),
            gas=self.config.tx.get_gas(),
            contract=constants.MAINNET_BRIDGE_CONTRACT_ADDRESS,
            contract_method=contract.functions.depositETH,
            contract_method_args=[round(self.config.tx.value * 0.95), 40000]
        )
        tx = Transaction(tx_config)
        receipt = tx.send(wait=True)

        if tx.config.hash:
            self.log('Transaction successfully sent')
            self.log(tx.config.hash.hex())

        return receipt
