import sqlite3

def createStockPrice():

    con = sqlite3.connect("./DB/stockPrice.db")
    cur  = con.cursor()

    create_table_sql ="""
    CREATE TABLE stockPrice (code TEXT,date TEXT, open REAL, high REAL, low REAL, close REAL,adjclose REAL,volume REAL,PRIMARY KEY(code, date))
    """

    cur.execute(create_table_sql)
    
    cur.close()
    con.close()
    
def createStockCodes():

    con = sqlite3.connect("./DB/stockPrice.db")
    cur  = con.cursor()

    create_table_sql ="""
    CREATE TABLE stockPrice (code TEXT,date TEXT, open REAL, high REAL, low REAL, close REAL,adjclose REAL,volume REAL,PRIMARY KEY(code, date))
    """

    cur.execute(create_table_sql)
    
    cur.close()
    con.close()
    
def createStockCreditBalances():

    con = sqlite3.connect("./DB/stockCreditBalances.db")
    cur  = con.cursor()

    create_table_sql ="""
    CREATE TABLE stockCreditBalances (code TEXT,date TEXT, buy_balance INTEGER, sell_balance INTEGER,PRIMARY KEY(code, date))
    """

    cur.execute(create_table_sql)
    
    cur.close()
    con.close()
    
if __name__ == '__main__':
    createStockCreditBalances()