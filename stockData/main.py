
pip install yfinance
pip install sqlalchemy
import yfinance as yf
from sqlalchemy import create_engine
def gethistory(stock_symbol):

    for stock in stock_symbol:
        if stock=="IDEA.NS":
            stock_name="VodafoneIdea"
        elif stock=="^NSEI":
            stock_name="Nifty50"
        else:
            stock_name=""

        history=yf.download(tickers=stock, period="max", interval="1d", actions=True,timeout=60)

        #history.to_csv(stock_name+".csv", encoding='utf-8')

        conn = create_engine('postgresql://username:password@database_connection_string:5432/stockdb')
        history.to_sql(stock_name, conn, index=False, if_exists='replace')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    symbols= ["IDEA.NS", "^NSEI"]
    gethistory(symbols)



