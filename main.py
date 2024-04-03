from lib.sql import insert
from lib.stockOp import getStockCodes,getStockInfo

df = getStockCodes.getStockCodeDataFrame()
codeList = df['code'].to_list()
insert.insertStockCode(df=df)

for code in codeList:
    stock = getStockInfo.stockInfo(code=code)
    stockPrice = stock.getStockPriceInfo(period='1d',interval='1d')
    insert.insertStockPrice(df=stockPrice)
    
    