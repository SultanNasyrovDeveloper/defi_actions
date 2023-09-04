from web3_utils import (
    Transaction, TransactionConfig, TransactionExecutionType,
    get_node_rpc_url, EVMChain, TransactionAmountWithGasConfig
)

from ..base import BaseActionConfig


class ScrollBridgeConfig(BaseActionConfig):

    tx: TransactionAmountWithGasConfig
