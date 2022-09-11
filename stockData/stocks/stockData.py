import yfinance as yf
import nsepy
from utils import utility
from datetime import date,timedelta
from constant import constants
import time


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
        history.rename(columns=constants.YFINANCE_COLUMN_NAMES,inplace=True)
        history.index.names=['trading_date']
        history.to_sql(stock_name, conn, index=True, if_exists='replace')

def getNseHistory(stock_symbol, conn):
        for stock in stock_symbol:
            print("Fetching Data for "+stock+" from NSE")
            index_stock_identifier=stock_symbol[stock]  #To identify whether it is an index or Equity
            stock_name_in_db=utility.getStockNameForDB(stock) #Remove Spaces

            history = nsepy.get_history(stock, start=utility.getDate(constants.TIME_DELTA), end=date.today(), index=index_stock_identifier) #Get Historical Records

            history.rename(columns=constants.NSE_COLUMN_NAMES, inplace=True) #Rename columnname for db
            history.index.names = ['trading_date']
            print("Loading Data for " + stock + " from NSE for the last "+constants.TIME_DELTA)
            history.to_sql(stock_name_in_db,conn,index=True, if_exists='append') #Append New Records
            time.sleep(15)


def cleanseData(stock_symbol,cursor):
    for stock in stock_symbol:
        stock_name_in_db = utility.getStockNameForDB(stock)
        for sqls in constants.CLEANSE_SQL:
            run_sql=constants.CLEANSE_SQL[sqls]
            run_sql=run_sql.replace("table_name",utility.getStockNameForDB(stock))
            print(run_sql)
            cursor.execute(run_sql)
