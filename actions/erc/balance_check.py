from django.utils import timezone
from web3 import Web3

from actions.base import BaseAction
from web3_utils.abi.erc20 import ERC20_TOKEN_ABI
from web3_utils.contracts import get_token_contract_address
from web3_utils.enums import EVMChain, ERC20Token
from web3_utils.types import EVMChainId, ERC20TokenId, Address
from web3_utils.utils import get_node_rpc_url

from .configs import (
    BalanceCheckConfig,
    ChainTokenBalance,
    TokenBalance,
    WalletBalance
)

NOT_ETHER_TOKENS = (
    ERC20Token.usdc.value, ERC20Token.usdt.value
)


class BalanceCheck(BaseAction):

    name = 'Balance Check'
    validator = BalanceCheckConfig
    config: BalanceCheckConfig

    def _perform_execution(self) -> WalletBalance:
        wallet_balance = WalletBalance()
        for chain in self.config.chains:
            chain_tokens_balance = ChainTokenBalance(id=chain.id)
            web3 = Web3(Web3.HTTPProvider(get_node_rpc_url(chain.id)))
            for token in chain.tokens:
                token_balance = TokenBalance(
                    id=token,
                    value=self.check_token_balance(
                        web3,
                        web3.to_checksum_address(self.execution.task.bot.wallet.address),
                        chain.id,
                        token
                    ),
                    updated=timezone.now().isoformat()
                )
                chain_tokens_balance.balances.append(token_balance)
            wallet_balance.chains.append(chain_tokens_balance)
        self.execution.task.bot.wallet.balance = wallet_balance.dict()
        self.execution.task.bot.wallet.save()
        return wallet_balance

    def check_token_balance(
        self,
        web3: Web3,
        address: Address,
        chain: EVMChainId,
        token: ERC20TokenId
    ) -> int:
        if token == ERC20Token.eth:
            balance = web3.eth.get_balance(web3.to_checksum_address(address))
        else:
            contract_address = get_token_contract_address(chain=chain, token=token)
            contract = web3.eth.contract(abi=ERC20_TOKEN_ABI, address=contract_address)
            balance = contract.functions.balanceOf(address).call()
        return balance
