from lib.sql import insert
from lib.stockOp import getStockCodes,getStockInfo

##create TBL & code insert
df = getStockCodes.getStockCodeDataFrame()
codeList = df['code'].to_list()
insert.insertStockCode(df=df)

##create TBL & stockPrice insert
for code in codeList:
    stock = getStockInfo.stockInfo(code=code)
    stockPrice = stock.getStockPriceInfo(period='20d',interval='1d')
    insert.insertStockPrice(df=stockPrice)


    