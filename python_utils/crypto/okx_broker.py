
import okx.MarketData as MarketData
import okx.Account as Account

from python_utils.crypto.models import Coin

class OkxBroker:
    """
    OKX API客户端
    """
    def __init__(self, api_key='-1', api_secret_key='-1', passphrase='-1', flag: str = '1') -> None:
        self.market_api = MarketData.MarketAPI(api_key=api_key, api_secret_key=api_secret_key, passphrase=passphrase, flag=flag)

    def get_tickers(self, instType: str = ''):
        return self.market_api.get_tickers(instType=instType)

    def get_ticker(self, coin: Coin):
        return self.market_api.get_ticker(instId=coin.value)

if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv()

    broker = OkxBroker(
        api_key=os.getenv("OKX_API_KEY"),
        api_secret_key=os.getenv("OKX_API_SECRET"),
        passphrase=os.getenv("OKX_API_PASSPHRASE"),
        flag=os.getenv("OKX_FLAG")
    )
    tickers = broker.get_tickers(instType='SPOT')
    print(tickers)

    ticker = broker.get_ticker(Coin.BTC)
    print(ticker)
