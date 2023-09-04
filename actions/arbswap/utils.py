from typing import Optional

from web3_utils.types import EVMChainId, ERC20TokenId, Address

from .constants import ARBSWAP_ROUTER_CONTRACT_ADDRESS_MAP


def get_router_address(chain: EVMChainId) -> Optional[Address]:
    return ARBSWAP_ROUTER_CONTRACT_ADDRESS_MAP.get(chain, None)
