from web3_utils.enums import EVMChain, ERC20Token
from web3_utils.types import (
    EVMChainId, ERC20TokenId, Address, Contract, ContractFunction
)
from .enums import StargateChain


MAINNET_ROUTER_ADDRESS = '0x8731d54E9D02c286767d56ac03e8037C07e01e98'
MAINNET_ETHERIUM_ROUTER_ADDRESS = '0x150f94B44927F078737562f0fcF3C95c01Cc2376'

BNB_ROUTER_ADDRESS = '0x4a364f8c717cAAD9A442737Eb7b8A55cc6cf18D8'

AVALANCHE_ROUTER_ADDRESS = '0x45A01E4e04F14f7A4a6702c74187c5F6222033cd'

FANTOM_ROUTER_ADDRESS = '0xAf5191B0De278C7286d6C7CC6ab6BB8A73bA2Cd6'

ARBITRUM_ROUTER_ADDRESS = '0x53Bf833A5d6c4ddA888F69c22C88C9f356a41614'
ARBITRUM_ETHERIUM_ROUTER_ADDRESS = '0xbf22f0f184bCcbeA268dF387a49fF5238dD23E40'

OPTIMISM_ROUTER_ADDRESS = '0xB0D502E938ed5f4df2E681fE6E419ff29631d62b'
OPTIMISM_ETHERIUM_ROUTER_ADDRESS = '0xB49c4e680174E331CB0A7fF3Ab58afC9738d5F8b'


CONTRACT_ADDRESS_MAP: dict[EVMChainId, [Address, Address]] = {
    EVMChain.mainnet: (MAINNET_ROUTER_ADDRESS, MAINNET_ETHERIUM_ROUTER_ADDRESS),
    EVMChain.arbitrum_one: (ARBITRUM_ROUTER_ADDRESS, ARBITRUM_ETHERIUM_ROUTER_ADDRESS),
    EVMChain.optimism: (OPTIMISM_ROUTER_ADDRESS, OPTIMISM_ETHERIUM_ROUTER_ADDRESS),
    EVMChain.binance_smart_chain: (BNB_ROUTER_ADDRESS, ),
    EVMChain.avalanche: (AVALANCHE_ROUTER_ADDRESS, ),
    EVMChain.fantom: (FANTOM_ROUTER_ADDRESS, ),
}

CHAIN_ID_MAP: dict[EVMChainId, EVMChainId] = {
    EVMChain.mainnet: StargateChain.mainnet,
    EVMChain.binance_smart_chain: StargateChain.binance_smart_chain,
    EVMChain.optimism: StargateChain.optimism,
    EVMChain.arbitrum_one: StargateChain.arbitrum_one,
    EVMChain.fantom: StargateChain.fantom,
    EVMChain.avalanche: StargateChain.avalanche,
    EVMChain.polygon: StargateChain.polygon
}

POOL_ID_MAP: dict[EVMChainId: dict[ERC20TokenId, int]] = {
    EVMChain.mainnet: {
        ERC20Token.eth: 13,
        ERC20Token.usdc: 1,
        ERC20Token.usdt: 2,
    },
    EVMChain.binance_smart_chain: {
        ERC20Token.eth: 13,
        ERC20Token.usdc: 1,
        ERC20Token.usdt: 2,
    },
    EVMChain.optimism: {
        ERC20Token.eth: 13,
        ERC20Token.usdc: 1,
    },
    EVMChain.arbitrum_one: {
        ERC20Token.eth: 13,
        ERC20Token.usdc: 1,
        ERC20Token.usdt: 2,
    },
    EVMChain.avalanche: {
        ERC20Token.usdc: 1
    },
    EVMChain.fantom: {
        ERC20Token.usdc: 1
    },
    EVMChain.polygon: {
        ERC20Token.usdc: 1,
        ERC20Token.usdt: 2,
    }
}



