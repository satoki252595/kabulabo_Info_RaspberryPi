import sqlite3

def createStockPrice():

    con = sqlite3.connect("./DB/stockPrice.db")
    cur  = con.cursor()

    create_table_sql ="""
    CREATE TABLE stockPrice (code TEXT,date TEXT, open REAL, high REAL, low REAL, close REAL,adjclose REAL,volume REAL,PRIMARY KEY(code, date))
    """

    cur.execute(create_table_sql)