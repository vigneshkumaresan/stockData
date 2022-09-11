from datetime import date,timedelta

def getDate(timeDelta):
    return date.today()-timedelta(days=timeDelta)

def getStockNameForDB(stock):
    return "nse_" + stock.replace(" ", "").lower()