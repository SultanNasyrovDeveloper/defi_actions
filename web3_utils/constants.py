from web3_utils.enums import ERC20Token, EVMChain
from web3_utils.types import ERC20TokenId, EVMChainId, Address


ChainTokenAddresses = dict[ERC20TokenId, Address]
ChainTokenMap = dict[EVMChainId, ChainTokenAddresses]

MAINNET_NODE_URL = 'https://mainnet.infura.io/v3/e8414f19a1c5421bb3dbc9911ee057a1'
MAINNET_GOERLI_NODE_URL = 'https://goerli.infura.io/v3/e8414f19a1c5421bb3dbc9911ee057a1'
ARBITRUM_ONE_NODE_URL = 'https://arbitrum-mainnet.infura.io/v3/e8414f19a1c5421bb3dbc9911ee057a1'
ARBITRUM_NOVA_NODE_URL = 'https://nova.arbitrum.io/rpc'
OPTIMISM_NODE_URL = 'https://optimism-mainnet.infura.io/v3/e8414f19a1c5421bb3dbc9911ee057a1'


MAINNET_CONTRACT_ADDRESS_MAP: ChainTokenAddresses = {
    ERC20Token.usdt: '0xdAC17F958D2ee523a2206206994597C13D831ec7',
    ERC20Token.usdc: '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'
}

ARBITRUM_CONTRACT_ADDRESS_MAP: ChainTokenAddresses = {
    ERC20Token.arb: '0x912CE59144191C1204E64559FE8253a0e49E6548',
    ERC20Token.usdc: '0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8',
    ERC20Token.usdt: '0xdAC17F958D2ee523a2206206994597C13D831ec7'
}

OPTIMISM_CONTRACT_ADDRESS_MAP: ChainTokenAddresses = {
    ERC20Token.usdc: '0x7F5c764cBc14f9669B88837ca1490cCa17c31607',
    ERC20Token.op: '0x4200000000000000000000000000000000000042',
    ERC20Token.usdt: '0x94b008aA00579c1307B0EF2c499aD98a8ce58e58'
}

ARBITRUM_NOVA_CONTRACT_ADDRESS_MAP: ChainTokenAddresses = {
    ERC20Token.eth: '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE',
    ERC20Token.usdc: '0x750ba8b76187092B0D1E87E28daaf484d1b5273b',
    ERC20Token.weth: '0x722E8BdD2ce80A4422E880164f2079488e115365',
    ERC20Token.arb: '0xf823C3cD3CeBE0a1fA952ba88Dc9EEf8e0Bf46AD'
}

CHAIN_TOKEN_MAP: ChainTokenMap = {
    EVMChain.mainnet: MAINNET_CONTRACT_ADDRESS_MAP,
    EVMChain.optimism: OPTIMISM_CONTRACT_ADDRESS_MAP,
    EVMChain.arbitrum_one: ARBITRUM_CONTRACT_ADDRESS_MAP,
    EVMChain.arbitrum_nova: ARBITRUM_NOVA_CONTRACT_ADDRESS_MAP
}