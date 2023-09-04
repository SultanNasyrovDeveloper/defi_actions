from web3_utils import Web3

from ..utils import get_node_rpc_url
from .configs import TransactionConfig
from .types import TransactionHash, TransactionReceipt


class Transaction:

    config: TransactionConfig

    def __init__(self, config: TransactionConfig):
        self.config = config

    def call(self) -> dict:
        if self.config.contract:
            web3 = Web3(Web3.HTTPProvider(get_node_rpc_url(self.config.chain)))
            if web3.is_connected():
                tx = self.config.contract_method(*(self.config.contract_method_args or []))
                return tx.call()
        # else raise

    def send(self, wait: bool = False) -> TransactionHash | TransactionReceipt:
        if self.config.contract:
            # get web3_utils
            web3 = Web3(Web3.HTTPProvider(get_node_rpc_url(self.config.chain)))
            if web3.is_connected():
                tx = self.config.contract_method(*self.config.contract_method_args)
                build_data = self.config.get_transaction_params(web3)
                built_tx = tx.build_transaction(build_data)
                signed_tx = web3.eth.account.sign_transaction(
                    built_tx,
                    self.config.wallet.personal_key
                )
                self.config.hash = web3.eth.send_raw_transaction(
                    signed_tx.rawTransaction
                )
                if wait:
                    return web3.eth.wait_for_transaction_receipt(self.config.hash)
                return self.config.hash

