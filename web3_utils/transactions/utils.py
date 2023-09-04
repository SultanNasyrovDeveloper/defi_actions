import random

from web3 import Web3

from web3_utils.utils import to_string_denomination

from ..types import Wei


def calculate_transaction_gas(max_gas: int) -> int:
    min_gas = round(max_gas * 0.9)
    return random.randint(min_gas, max_gas)


def calculate_random_transaction_value(config) -> Wei:
    """
    Calculate random allowed to use transaction value.

    Args:
        config: Amount config.

    Returns:
        transaction_value(int): in wei.
    """
    # TODO: Check if safe gas more than max gas and stop transaction execution
    if config.min_amount and config.max_amount:
        min_in_wei = Web3.to_wei(
            config.min_amount,
            to_string_denomination(config.min_amount_unit)
        )
        max_in_wei = Web3.to_wei(
            config.max_amount,
            to_string_denomination(config.max_amount_unit)
        )
        return random.randint(min_in_wei, max_in_wei)
    return 0
