

import yfinance as yf
import db
import constant
from sqlalchemy import create_engine
def gethistory(stock_symbol):

    for stock in stock_symbol:
        if stock=="IDEA.NS":
            stock_name="vodafoneidea"
        elif stock=="^NSEI":
            stock_name="nifty50"
        else:
            stock_name=""

        history=yf.download(tickers=stock, period="max", interval="1d", actions=True,timeout=60)
        history.rename(columns={'Open':'open',
                                'Close':'close',
                                'High':'high',
                                'Low':'low',
                                'Adj Close':'adj_close',
                                'Volume':'volume',
                                'Dividends':'dividends',
                                'Stock Splits':'stock_splits'
                                }
                       ,inplace=True)
        history.index.names=['trading_date']

        conn = create_engine('postgresql://username:password@dbname:5432/stockdb')
        history.to_sql(stock_name, conn, index=True, if_exists='replace')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    symbols= ["IDEA.NS", "^NSEI"]
    gethistory(symbols)


