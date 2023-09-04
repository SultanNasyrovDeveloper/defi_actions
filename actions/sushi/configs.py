import decimal

from actions.configs import BaseActionConfig
from actions.types import Address, ERC20TokenId, ChainId


class SushiSwapConfig(BaseActionConfig):

    chain: ChainId = 1
    from_token: ERC20TokenId = 1
    to_token: ERC20TokenId = 1
    amount_int: decimal.Decimal = 0
    amount_out_min: decimal.Decimal = 0
    to: Address = ''
