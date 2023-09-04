from typing import Optional

from web3_utils.types import EVMChainId, Address

from . import constants


def get_contract_address(chain: EVMChainId) -> Optional[Address]:
    return constants.BRIDGE_CONTRACT_ADDRESS_MAP.get(chain, None)