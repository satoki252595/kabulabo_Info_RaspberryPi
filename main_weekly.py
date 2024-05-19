from lib.sql import insert
from lib.stockOp import getStockCodes,getStockInfo

#create TBL & code insert
df = getStockCodes.getCreditBalancesInfo(1)
df = getStockCodes.getCreditBalancesInfo(2)
df = getStockCodes.getCreditBalancesInfo(3)
df = getStockCodes.getCreditBalancesInfo(4)
df = getStockCodes.getCreditBalancesInfo(5)
insert.insertStockCreditBalances(df)