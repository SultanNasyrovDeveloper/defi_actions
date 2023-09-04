from pydantic import BaseModel
from web3 import Web3

from actions.configs import BaseActionConfig
from web3_utils import TransactionAmountWithGasConfig, TokenTransactionAmount
from web3_utils.enums import ERC20Token, EVMChain, EtheriumDenomination
from web3_utils.types import Address

from .enums import StargateChain


class StargateFinanceSwapConfig(BaseActionConfig):

    # contract interaction config
    from_chain: EVMChain
    to_chain: EVMChain
    from_token: ERC20Token
    to_token: ERC20Token
    amount_ld: TokenTransactionAmount

    # transaction config
    # transaction value is used to pay fee for cross chain money move
    tx: TransactionAmountWithGasConfig

    class Config:
        arbitrary_types_allowed = True


class SwapFunctionData(BaseModel):

    destination_chain: StargateChain
    source_pool: int
    destination_pool: int
    refund_address: Address
    amount: int
    amount_min: int
    lzt_params: tuple = ({
        'dstGasForCall': 0,
        'dstNativeAmount': 0,
        'dstNativeAddr': '0x0000000000000000000000000000000000000001'
    })
    to: Address
    payload: str = '0x'

    def to_list(self):
        return [
            self.destination_chain.value,
            self.source_pool,
            self.destination_pool,
            Web3.to_checksum_address(self.refund_address),
            self.amount,
            self.amount_min,
            self.lzt_params,
            self.to,
            b'',
        ]


class SwapEtheriumFunctionData(BaseModel):

    destination_chain: StargateChain
    refund_address: Address
    to: Address
    amount_ld: int
    min_amount_ld: int

    def to_list(self):
        return [
            self.destination_chain.value,
            self.refund_address,
            Web3.to_bytes(text=self.to),
            self.amount_ld,
            self.min_amount_ld
        ]

