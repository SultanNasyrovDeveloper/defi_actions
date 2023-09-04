import random
from typing import Any, Optional

from pydantic import BaseModel
from web3 import Web3
from web3.contract.contract import ContractFunction

from web3_utils.enums import EVMChain, EtheriumDenomination, ERC20Token
from web3_utils.types import Address
from ..wallet.models import Wallet

from .enums import TransactionExecutionType
from .types import TransactionParams, TransactionHash
from .utils import (
    calculate_random_transaction_value,
    calculate_transaction_gas,
    to_string_denomination
)


AMOUNT_FIELDS = {'min_amount', 'min_amount_unit', 'max_amount', 'max_amount_unit', 'value'}
GAS_FIELDS = {
    'max_gas', 'max_gas_price',
    'max_gas_price_unit', 'max_priority_gas_price',
    'max_priority_gas_price', 'max_priority_gas_price_unit',
}

TOKEN_DECIMALS_MAP = {
    ERC20Token.usdc: 6
}


class TransactionAmountConfig(BaseModel):

    # percentage: int
    min_amount: float = 0
    min_amount_unit: EtheriumDenomination = EtheriumDenomination.ether.value
    max_amount: float = 0
    max_amount_unit: EtheriumDenomination = EtheriumDenomination.ether.value
    value: Optional[int]


class TransactionGasConfig(BaseModel):

    max_gas: int = 0
    max_gas_price: float = 0
    max_gas_price_unit: EtheriumDenomination = EtheriumDenomination.gwei.value
    max_priority_gas_price: Optional[float] = 0
    max_priority_gas_price_unit: Optional[EtheriumDenomination] = EtheriumDenomination.gwei.value


class TransactionAmountWithGasConfig(TransactionAmountConfig, TransactionGasConfig):

    def get_amount(self) -> TransactionAmountConfig:
        return TransactionAmountConfig(**self.dict(include=AMOUNT_FIELDS))

    def get_gas(self) -> TransactionGasConfig:
        return TransactionGasConfig(**self.dict(include=GAS_FIELDS))

    def calculate_random_value(self):
        self.value = calculate_random_transaction_value(self)


class TokenTransactionAmount(TransactionAmountConfig):

    min_amount_unit: ERC20Token
    max_amount_unit: Optional[ERC20Token]

    def calculate_random_value(self):
        min_amount = self.min_amount * (10 ** TOKEN_DECIMALS_MAP[self.min_amount_unit])
        max_amount = self.max_amount * (10 ** TOKEN_DECIMALS_MAP[self.max_amount_unit])
        self.value = random.randint(min_amount, max_amount)
        return self.value


class TokenTransactionAmountWithGasConfig(
    TransactionAmountWithGasConfig,
    TokenTransactionAmount,
    TransactionGasConfig
): pass


class TransactionConfig(BaseModel):

    # transaction
    wallet: Wallet
    nonce: Optional[int] = None
    hash: Optional[TransactionHash] = None
    type: TransactionExecutionType = TransactionExecutionType.call  # call or payable
    chain: EVMChain
    to: Optional[Address]
    amount: TransactionAmountConfig
    gas: TransactionGasConfig

    # contract
    contract: Optional[Address]
    contract_method: Optional[ContractFunction]
    contract_method_args: Optional[list[Any]] = []

    # validators

    class Config:
        arbitrary_types_allowed = True

    # validate that from and to configured if not contract method
    # contract method and contract method args specified if contract not None

    def get_transaction_params(self, web3: Web3) -> TransactionParams:
        nonce = self.nonce
        if not nonce:
            nonce = web3.eth.get_transaction_count(
                web3.to_checksum_address(self.wallet.address)
            )
            self.nonce = nonce
        value = self.amount.value
        if value is None:
            value = calculate_random_transaction_value(self.amount)
            self.amount.value = value
        return {
            'from': web3.to_checksum_address(self.wallet.address),
            'nonce': nonce,
            'value': value,
            'gas': calculate_transaction_gas(self.gas.max_gas),
            'maxFeePerGas': web3.to_wei(
                self.gas.max_gas_price,
                to_string_denomination(self.gas.max_gas_price_unit)
            ),
            **({'maxPriorityFeePerGas': web3.to_wei(
                self.gas.max_priority_gas_price,
                to_string_denomination(self.gas.max_priority_gas_price_unit)
            )} if self.gas.max_priority_gas_price else {})
        }