from pydantic import BaseModel
from web3 import Web3

from web3_utils import (
    Address,
    EVMChainId,
    TransactionAmountWithGasConfig,
    TransactionAmountConfig,
    calculate_random_transaction_value
)
from ..base import BaseActionConfig
from . import constants


class LayerZeroTestnetBridgeConfig(BaseActionConfig):

    from_chain: EVMChainId
    amount: TransactionAmountConfig
    tx: TransactionAmountWithGasConfig


class TestnetBridgeArgs(BaseModel):

    amount: TransactionAmountConfig
    destination_chain: EVMChainId = 154
    to: Address
    refund_address: Address

    @classmethod
    def from_config(cls, config: LayerZeroTestnetBridgeConfig):
        return cls(
            amount=config.amount,
            to=Web3.to_checksum_address(config.wallet.address),
            refund_address=Web3.to_checksum_address(config.wallet.address)
        )

    def to_list(self):
        if not self.amount.value:
            self.amount.value = calculate_random_transaction_value(self.amount)
        return [
            self.amount.value,
            round(self.amount.value * constants.BRIDGE_GOETH_TO_ETH_RATE * 0.9),
            self.destination_chain,
            Web3.to_checksum_address(self.to),
            Web3.to_checksum_address(self.refund_address if self.refund_address else self.to),
            Web3.to_checksum_address('0x0000000000000000000000000000000000000000'),
            b''
        ]

