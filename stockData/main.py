


import db.createConnection as connect
import stocks.stockData as sd
from constant import constants

import nsepy
from datetime import date,timedelta

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        """
        #To get the data from Yahoo Finance
        symbols= constants.yfinance_symbols #To get the data from Yahoo Finance
        conn=connect.getConnection()
        sd.getYahooFinanceHistory(symbols,conn) #To get the data from Yahoo Finance
        connect.closeConnection(conn)
        """

        symbols = constants.NSE_SYMBOLS  # To get the data from NSE
        conn = connect.getConnection()
        sd.getNseHistory(symbols, conn)

    finally:
        connect.closeConnection(conn)

    try:
        connection,cursor=connect.pgCursor()
        sd.cleanseData(symbols,cursor)

    finally:
        connect.pgClose(connection,cursor)

