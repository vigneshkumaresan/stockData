#DB Parameters
DB_URL=""
DB_NAME="stockdb"
PORT="5432"
USERNAME="postgres"
PASSWORD=""

#Stock Data Parameters
YFINANCE_SYMBOLS= ["IDEA.NS", "^NSEI","^INDIAVIX"]
NSE_SYMBOLS= {"IDEA":False, "NIFTY 50":True,"INDIAVIX":True} #True indicates Index, False Indicates Equity
NSE_DATA_TABLE_NAME="nse_stock_index_vix_data"
NSE_COLUMN_NAMES={'Symbol': 'symbol',
                  'Series': 'series',
                  'Prev Close': 'prev_close',
                  'Open': 'open',
                  'High': 'high',
                  'Low': 'low',
                  'Last': 'last',
                  'Close': 'close',
                  'VWAP': 'vwap',
                  'Volume': 'volume',
                  'Turnover': 'turnover',
                  'Trades': 'trades',
                  'Deliverable Volume': 'deliverable_volume',
                  '%Deliverable': 'percentage_deliverable',
                  'Previous': 'previous_close',
                  'Change': 'change',
                  '%Change': 'percentage_change'
                  }
YFINANCE_COLUMN_NAMES={'Open': 'open',
                       'Close': 'close',
                       'High': 'high',
                       'Low': 'low',
                       'Adj Close': 'adj_close',
                       'Volume': 'volume',
                       'Dividends': 'dividends',
                       'Stock Splits': 'stock_splits'
                       }


#Cleanse the data parameters
CLEANSE_SQL={'sql_string1': 'delete from table_name a using table_name b where a.ctid>b.ctid and a.trading_date =b.trading_date',
             'sql_string2': 'delete from table_name a where open is null'
             }


#Retention Parameters
#TIME_DELTA=10000
TIME_DELTA=5
