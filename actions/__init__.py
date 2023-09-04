from typing import Optional

from actions.enums import ActionEnum
from actions.base import BaseAction
from actions.arbswap.swap import ArbSwapAction
from actions.erc.approve import ApproveAction
from actions.erc.balance_check import BalanceCheck
from actions.scroll.bridge import ScrollBridge
from actions.stargate.swap import StargateFinanceSwap
from actions.layer_zero.testnet_bridge import LayerZeroTestnetBridge


action_class_map = {
    2: BalanceCheck,
    3: ApproveAction,
    4: ArbSwapAction,
    5: StargateFinanceSwap,
    6: LayerZeroTestnetBridge,
    7: ScrollBridge
}


def create_action(action: int, **kwargs) -> Optional[BaseAction]:
    class_ = action_class_map.get(action, None)
    config = kwargs.pop('config')
    return (
        class_(config=class_.validator(**config), **kwargs)
        if class_
        else None
    )
