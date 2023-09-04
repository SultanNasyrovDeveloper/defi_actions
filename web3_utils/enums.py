from enum import IntEnum


class EVMChain(IntEnum):

    mainnet = 1
    goerli = 5
    binance_smart_chain = 56
    arbitrum_one = 42161
    arbitrum_nova = 42170
    optimism = 10
    fantom = 250
    avalanche = 43114
    polygon = 137


class ERC20Token(IntEnum):

     eth = 1
     arb = 2
     op = 3
     bnb = 4
     usdc = 5
     usdt = 6
     weth = 7


class EtheriumDenomination(IntEnum):
    """
    Wei (wei): For Wei Dai, who formulated the concepts of all modern cryptocurrencies—best known as the creator of the predecessor to Bitcoin, B-money.
    Kwei (babbage): For Charles Babbage, a mathematician, philosopher, inventor, and mechanical engineer—designed the first automatic computing engines.
    Mwei (lovelace): For Ada Lovelace, mathematician, writer, and computer programmer—she wrote and published the first algorithm.
    Gwei (shannon): For Claude Shannon, an American mathematician, cryptographer, and crypto-analysis guru—also known as "the father of information theory."
    Twei (szabo): For Nick Szabo, a computer scientist, legal scholar, and cryptographer—known for his pioneering research in digital contracts and digital currency.
    Pwei (finney): For Hal Finney, a computer scientist and cryptographer—he was one of the early developers of Bitcoin, and alleged to be the first human to receive a bitcoin from Satoshi Nakamoto, the named founder of Bitcoin.
    Ether (buterin): For Vitalik Buterin, a programmer and writer—he created Ethereum.
    """

    ether = 1
    pwei = 2
    twei = 3
    gwei = 4
    mwei = 5
    kwei = 6
    wei = 7