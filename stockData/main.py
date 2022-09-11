


import db.createConnection as connect
import stocks.stockData as sd
from constant import constants

import nsepy
from datetime import date

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    symbols= constants.yfinance_symbols
    conn=connect.getConnection()
    sd.getYahooFinanceHistory(symbols,conn)
    connect.closeConnection(conn)



    #stock=nsepy.get_history("IDEA",start=date(1900,1,1),end=date.today(),index=False)
    #stock = nsepy.get_history("NIFTY 50", start=date(2007, 1, 1), end=date.today(),index=True)
    #stock = nsepy.get_history("INDIAVIX", start=date(1991, 1, 1), end=date.today(),index=True)
    #print(stock)

