from web3_utils import Web3

from web3_utils import Transaction, TransactionConfig, get_node_rpc_url

from ..base import BaseAction
from . import abi, configs, utils


class LayerZeroTestnetBridge(BaseAction):

    name = 'Layer Zero Testnet Bridge'
    validator = configs.LayerZeroTestnetBridgeConfig
    config: configs.LayerZeroTestnetBridgeConfig

    def _perform_execution(self):
        """
        Layer zero testnet bridge action.
        """
        contract_address = utils.get_contract_address(self.config.from_chain)
        web3 = Web3(Web3.HTTPProvider(get_node_rpc_url(self.config.from_chain)))
        contract = web3.eth.contract(
            address=contract_address,
            abi=abi.TESTNET_BRIDGE_CONTRACT_ABI
        )
        contract_method = contract.functions.swapAndBridge
        contract_method_args = configs.TestnetBridgeArgs.from_config(self.config)

        transaction_config = TransactionConfig(
            wallet=self.config.wallet,
            amount=self.config.tx.get_amount(),  # TODO: Smth wrong with naming
            type=2,
            gas=self.config.tx.get_gas(),
            chain=self.config.from_chain,
            contract=contract_address,
            contract_method=contract_method,
            contract_method_args=contract_method_args.to_list(),
        )
        transaction = Transaction(transaction_config)
        receipt = transaction.send(wait=True)
        self.log(receipt.transactionHash.hex())
