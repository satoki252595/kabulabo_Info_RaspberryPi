import pandas as pd
import sqlite3

##絶対参照にした方が良い？
from ..stockOp.getStockCodes import getStockCodeDataFrame
from ..stockOp.getStockInfo import stockInfo

def insertStockPrice(code:str):

    #connection確立
    con = sqlite3.connect("./DB/stockPrice.db")

    stock = stockInfo(code)
    df = stock.getStockPriceInfo(period='1mo',interval='1d')
    
    #一括書込み
    df.to_sql('stockPrice',con,if_exists='append',index=None)

    #commit
    con.commit()
    con.close()

def insertStockCode():

    #connection確立
    con = sqlite3.connect("./DB/stockCode.db")

    #一括書込み
    df = getStockCodeDataFrame()
    df.to_sql('stockCode',con,if_exists='replace',index=None)

    #commit
    con.commit()
    con.close()
    
if __name__ == '__main__':
    
    insertStockCode()
    insertStockPrice('1414')