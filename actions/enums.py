from enum import IntEnum


class ActionEnum(IntEnum):

    erc_balance_check = 1
    erc_multiple_balance_check_simple = 2
    sushi_swap = 3
    arbswap = 4
    stargate_swap = 5

    @staticmethod
    def choices():
        return (
            (1, 'ERC20 Mainnet Balance Check'),
            (2, 'ERC20 Multiple Balance Check Simple'),
            (3, 'Sushi swap'),
            (4, 'Arbswap'),
            (5, 'Stargate swap')
        )


class EVMChain(IntEnum):

    mainnet = 1
    binance_smart_chain = 56
    arbitrum_one = 42161
    arbitrum_nova = 42170
    optimism = 10


class ERC20Token(IntEnum):

     eth = 1
     arb = 2
     op = 3
     bnb = 4
     usdc = 5
     usdt = 6
     weth = 7
