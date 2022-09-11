import yfinance as yf
import nsepy
from datetime import date
def getYahooFinanceHistory(stock_symbol,conn):
    #Below is the code to get the data from Yahoo Finance
    for stock in stock_symbol:
        if stock=="IDEA.NS":
            stock_name="vodafoneidea"
        elif stock=="^NSEI":
            stock_name="nifty50"
        elif stock=="^INDIAVIX":
            stock_name="indiavix"
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
        history.to_sql(stock_name, conn, index=True, if_exists='replace')

#def getNseHistory(stock_symbol, conn):
#        #history=nsepy.get_history()