from typing import Optional

from web3_utils.enums import EVMChain, EtheriumDenomination
from web3_utils.types import EVMChainId

from .. import constants


node_url_map: dict[EVMChainId, str] = {
    EVMChain.mainnet: constants.MAINNET_NODE_URL,
    EVMChain.goerli: constants.MAINNET_GOERLI_NODE_URL,
    EVMChain.arbitrum_one: constants.ARBITRUM_ONE_NODE_URL,
    EVMChain.optimism: constants.OPTIMISM_NODE_URL,
    EVMChain.arbitrum_nova: constants.ARBITRUM_NOVA_NODE_URL,
}

DENOMINATION_STRING_MAP = {
    EtheriumDenomination.ether: 'ether',
    EtheriumDenomination.gwei: 'gwei',
    EtheriumDenomination.wei: 'wei'
}


def get_node_rpc_url(chain_id: EVMChainId) -> Optional[str]:
    url = node_url_map.get(chain_id, None)
    return url


def to_string_denomination(denomination: EtheriumDenomination) -> str:
    return DENOMINATION_STRING_MAP.get(denomination, None)
