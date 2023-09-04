from typing import Optional

from web3 import Web3

from web3_utils.constants import CHAIN_TOKEN_MAP
from web3_utils.types import ERC20TokenId, EVMChainId, Address


def get_token_contract_address(chain: EVMChainId, token: ERC20TokenId) -> Optional[Address]:
    """
    Get ERC20 token address.
    """
    chain_tokens = CHAIN_TOKEN_MAP.get(chain, None)
    token_address = chain_tokens.get(token, None) if chain_tokens else None
    return Web3.to_checksum_address(token_address) if token_address else None
