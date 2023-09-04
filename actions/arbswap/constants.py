from web3_utils.enums import EVMChain
from web3_utils.types import Address, EVMChainId


ARBSWAP_ROUTER_CONTRACT_ADDRESS_MAP: dict[EVMChainId, Address] = {
    EVMChain.arbitrum_nova: '0x67844f0f0dd3D770ff29B0ACE50E35a853e4655E',
    EVMChain.arbitrum_one: '0x6947A425453D04305520E612F0Cb2952E4D07d62'
}
