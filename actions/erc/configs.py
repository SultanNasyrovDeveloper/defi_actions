from pydantic import BaseModel

from web3_utils import (
    TokenTransactionAmountWithGasConfig
)
from web3_utils.enums import EVMChain, ERC20Token
from web3_utils.types import Address, ERC20TokenId

from ..configs import BaseActionConfig


class ChainTokens(BaseModel):

    id: EVMChain
    tokens: list[ERC20Token]


class BalanceCheckConfig(BaseModel):

    chains: list[ChainTokens]

    class Config:
        arbitrary_types_allowed = True


class TokenBalance(BaseModel):

    id: ERC20Token
    value: float  # in ether
    updated: str


class ChainTokenBalance(BaseModel):

    id: EVMChain
    balances: list[TokenBalance] = []  # in wei


class WalletBalance(BaseModel):

    chains: list[ChainTokenBalance] = []


class ApproveConfig(BaseActionConfig):

    chain: EVMChain
    token: ERC20TokenId
    spender: Address
    amount: TokenTransactionAmountWithGasConfig
