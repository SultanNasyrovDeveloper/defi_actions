from typing import Optional

from web3_utils import Web3

from web3_utils.enums import EVMChain, ERC20Token
from web3_utils.types import (
    EVMChainId, ERC20TokenId, Contract, ContractFunction
)
from . import abi, constants, configs


def get_stargate_chain_id(chain_id: EVMChain) -> Optional[EVMChain]:
    """
    Get Stargate Finance internal chain id.
    https://stargateprotocol.gitbook.io/stargate/developers/chain-ids

    Args:
        chain_id(int): chain id from web3_utils directory.

    Returns:
        chain_id(int?): stargate internal chain id.
    """
    return constants.CHAIN_ID_MAP.get(chain_id, None)


def get_stargate_pool_id(chain_id: EVMChain, token: ERC20Token) -> Optional[int]:
    """
    Get Stargate Finance Pool id.
    https://stargateprotocol.gitbook.io/stargate/developers/pool-ids
    """
    chain_pools_map = constants.POOL_ID_MAP.get(chain_id, {})
    return chain_pools_map.get(token, None)


def get_stargate_router_contract(
    web3: Web3,
    chain_id: EVMChainId,
    from_token: ERC20TokenId
) -> Optional[Contract]:
    """
    Get proper Stargate Finance router contract.

    Args:
        web3:
        chain_id:
        from_token:

    Returns:
        router contract: etherium or swap router.
    """
    contract_abi = (
        abi.STARGATE_ETHERIUM_ROUTER_ABI
        if from_token == ERC20Token.eth
        else abi.STARGATE_ROUTER_ABI
    )
    contract_addresses = constants.CONTRACT_ADDRESS_MAP.get(chain_id, None)
    if not contract_addresses:
        return None
    target_address = (
        contract_addresses[0]
        if from_token != ERC20Token.eth
        else contract_addresses[1]
    )
    contract = web3.eth.contract(abi=contract_abi, address=target_address)
    return contract


def get_stargate_swap_method(
    contract: Contract,
    from_token: ERC20TokenId
) -> Optional[ContractFunction]:
    if from_token == ERC20Token.eth:
        return contract.functions.swapETH
    return contract.functions.swap


def get_stargate_swap_method_args(
    config: configs.StargateFinanceSwapConfig,
) -> configs.SwapFunctionData | configs.SwapEtheriumFunctionData:
    if config.from_token == ERC20Token.eth:
        return configs.SwapEtheriumFunctionData(
            destination_chain=get_stargate_chain_id(config.to_chain),
            refund_address=config.wallet.address,
            to=config.wallet.address,
            amount_ld=config.amount_ld.value,
            min_amount_ld=round(config.amount_ld.value * 0.9)
        )
    return configs.SwapFunctionData(
        destination_chain=get_stargate_chain_id(config.to_chain),
        source_pool=get_stargate_pool_id(config.from_chain, config.from_token),
        destination_pool=get_stargate_pool_id(config.to_chain, config.to_token),
        refund_address=config.wallet.address,
        amount=config.amount_ld.value,
        amount_min=round(config.amount_ld.value * 0.9),
        to=config.wallet.address
    )
