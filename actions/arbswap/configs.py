import random

from pydantic import BaseModel
from web3 import Web3

from actions.configs import BaseActionConfig
from web3_utils import (
    TransactionAmountWithGasConfig, Wei, Address, EVMChainId,
    get_token_contract_address, calculate_random_transaction_value
)
from web3_utils.enums import ERC20Token, EVMChain


MIN_RETURN = 0.95


def wei_to_usdc(amount: Wei) -> int:
    one_ether_in_usdc = 1_800_000_000
    amount_in_ether = Web3.from_wei(amount, 'ether')
    amount_in_usdc_as_decimal = one_ether_in_usdc * amount_in_ether
    amount_in_usdc_as_int = round(amount_in_usdc_as_decimal)
    return amount_in_usdc_as_int


class ArbSwapActionConfig(BaseActionConfig):

    chain: EVMChainId = EVMChain.arbitrum_nova
    from_token: ERC20Token
    to_token: ERC20Token
    amount: TransactionAmountWithGasConfig


class ArbswapMethodArgs(BaseModel):

    source_token: Address
    destination_token: Address
    amount: Wei
    min_return: Wei
    flag: int = 1

    @classmethod
    def from_action_config(cls, config: ArbSwapActionConfig) -> 'ArbswapMethodArgs':
        if not config.amount.value:
            config.amount.value = calculate_random_transaction_value(config.amount)
        amount = int(
            wei_to_usdc(config.amount.value)
            if config.from_token == ERC20Token.usdc
            else config.amount.value
        )
        min_return = int(
            wei_to_usdc(config.amount.value)
            if config.to_token == ERC20Token.usdc
            else config.amount.value
        ) * MIN_RETURN
        return cls(
            source_token=get_token_contract_address(
                chain=config.chain,
                token=config.from_token
            ),
            destination_token=get_token_contract_address(
                chain=config.chain,
                token=config.to_token
            ),
            amount=amount,
            min_return=min_return,
            flag=1
        )

    def to_list(self):
        return [
            Web3.to_checksum_address(self.source_token),
            Web3.to_checksum_address(self.destination_token),
            self.amount,
            self.min_return,
            self.flag
        ]