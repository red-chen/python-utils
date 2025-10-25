
from mailbox import BabylMessage
from pydantic import BaseModel, Field
from enum import Enum, auto


class Symbol(str, Enum):
    """股票或期权合约代码"""
    SPY = "SPY"
    QQQ = "QQQ"
    TSLA = "TSLA"
    NVDA = "NVDA"
    AAPL = "AAPL"
    PLTR = "PLTR"
    BABA = "BABA"

class OptionType(str, Enum):
    """期权类型枚举"""
    PUT = "put"   # 看跌期权
    CALL = "call" # 看涨期权
    
class Option(BaseModel):
    """合约信息"""
    symbol: str = Field(default="", description="合约代码")
    expiry: str = Field(default="", description="到期日期")
    strike: float = Field(default=0.0, description="行权价格")
    put_call: str = Field(default="", description="看涨/看跌 (call/put)")
    currency: str = Field(default="", description="货币代码")
    name: str = Field(default="", description="合约名称")
    identifier: str = Field(default="", description="合约标识符")

    status: int = Field(default=0, description="合约状态")
    trade: bool = Field(default=False, description="是否可交易")
    shortable: bool = Field(default=False, description="是否可做空（对期权而言，通常指能否卖出开仓，即“裸卖”或“备兑”）")
    support_overnight_trading: bool = Field(default=False, description="是否支持盘后/隔夜交易（美股期权通常不支持")
    support_fractional_share: bool = Field(default=False, description="是否支持碎股交易（期权最小单位为 1 张，不支持碎股")

    @classmethod
    def from_json(cls, json_data: dict) -> 'Option':
        """从JSON对象构建Option实例"""
        return cls.model_validate(json_data)

    