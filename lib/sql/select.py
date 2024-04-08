import pandas as pd
import sqlite3

def selectStockPrice(df:pd.core.frame.DataFrame):

    #connection確立
    con = sqlite3.connect("./DB/stockPrice.db")
    
    #一括書込み
    df.to_sql('stockPrice',con,if_exists='append',index=None)

    #commit
    con.commit()
    con.close()

if __name__ == '__main__':
    selectStockPrice()