import pandas as pd
import yfinance

class stockInfo(object):

    def __init__(self,code:str):
        self.code = code
        
    def getStockPriceInfo(self,period:str,interval:str) -> pd.core.frame.DataFrame:
        
        '''
        period：期間、interval：間隔

        '1m','1h','1d','1wk','1mo','1y','max'　などのバリュー値を引数に取れる。        
        '''

        # DataFrameを作成します
        table_name = "stockPrice"
        df = yfinance.download(self.code + ".T", period=period,interval=interval)

        #indexを最初の列に挿入
        df.reset_index(inplace= True)
        df = df.rename(columns={'index': 'date'})
        #codeを最初の列に挿入
        df.insert(0, 'code', self.code)

        #列名の変更
        df.columns = ['code', 'date', 'open', 'high', 'low', 'close', 'adjclose', 'Volume']

        #'date'列をdatetime->strへ型変換
        df['date'] = df['date'].astype(str)

        #'-'はバイト数を消費するので削除しておく。
        df['date'] = df['date'].str.replace('-', '')

        #adjclose列の小数点第2位以下を丸め込む
        df['adjclose'] = df['adjclose'].round(2)
        
        return df