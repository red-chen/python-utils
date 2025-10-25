from enum import Enum, auto

class Coin(str, Enum):
    """加密货币代码"""
    BTC = "BTC"
    ETH = "ETH"
    USDT = "USDT"
    USDC = "USDC"
    BNB = "BNB"
    SOL = "SOL"
    ADA = "ADA"
    DOT = "DOT"
    LTC = "LTC"
    XRP = "XRP"