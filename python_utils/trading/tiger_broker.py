"""
老虎证券API客户端

基于Pydantic V2的数据验证和处理。
"""

from optparse import Option
from tigeropen.common.consts import (Language, # 语言
                                Market,        # 市场
                                BarPeriod,     # k线周期
                                QuoteRight, SecurityType)    # 复权类型
from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.quote.quote_client import QuoteClient
from tigeropen.trade.trade_client import TradeClient

from python_utils.trading.models import Option, OptionType

class TigerBroker:
    """
    老虎证券API客户端

    import os
    from dotenv import load_dotenv
    load_dotenv()
    
    config = TigerOpenClientConfig()

    config.tiger_id = os.getenv("TIGER_ID")
    config.account = os.getenv("TIGER_ACCOUNT")
    config.private_key = os.getenv("TIGER_PRIVATE_KEY")

    broker = TigerBroker(config)
    quote = broker.get_stock_briefs(['QQQ'])
    print(quote)
    """
    def __init__(self, config: TigerOpenClientConfig):
        self.config = config
        self.quote_client = QuoteClient(config)
        self.trade_client = TradeClient(config)

    def get_stock_briefs(self, symbols: list[str]) -> str:
        """获取股票实时报价"""
        return self.quote_client.get_stock_briefs(symbols)

    def get_option(self, symbol: str, expiry: str, strike: float, option_type: OptionType) -> Option:
        """获取合约信息，返回Option对象"""          
        contract = self.trade_client.get_contract(
            symbol,
            sec_type=SecurityType.OPT,
            expiry=expiry,
            strike=strike,
            put_call=option_type.value)
            
        # 将字典序列化为JSON字符串
        return Option.from_json(contract.__dict__)

if __name__ == "__main__":
    import os
    import json
    from dotenv import load_dotenv
    load_dotenv()
    
    config = TigerOpenClientConfig()

    config.tiger_id = os.getenv("TIGER_ID")
    config.account = os.getenv("TIGER_ACCOUNT")
    config.private_key = os.getenv("TIGER_PRIVATE_KEY")

    broker = TigerBroker(config)
    op = broker.get_option('SPY', '20251027', 680.0, OptionType.CALL)
    print(op.model_dump_json())

