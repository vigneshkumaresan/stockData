


import db.createConnection as connect
import stocks.stockData as sd
from constant import constants


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    symbols= constants.symbols
    conn=connect.getConnection()
    sd.gethistory(symbols,conn)
    connect.closeConnection(conn)


