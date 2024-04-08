from lib.sql import insert
from lib.stockOp import getStockCodes,getStockInfo

#create TBL & code insert
df = getStockCodes.getCreditBalancesInfo(1)
insert.insertStockCreditBalances(df)