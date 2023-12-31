from web3_utils.enums import EVMChain


ARBITRUM_BRIDGE_ADDRESS = '0x0A9f824C05A74F577A536A8A0c673183a872Dff4'
MAINNET_BRIDGE_ADDRESS = ''

BRIDGE_GOETH_TO_ETH_RATE = 14000

BRIDGE_CONTRACT_ADDRESS_MAP = {
    EVMChain.arbitrum_one: ARBITRUM_BRIDGE_ADDRESS
}