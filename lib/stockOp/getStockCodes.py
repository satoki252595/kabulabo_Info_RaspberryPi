import pandas as pd
import re
import pandas as pd
import urllib.request

#セキュリティ的にだめ！！（一時凌ぎ）
#https://qiita.com/shutokawabata0723/items/9733a7e640a175c23f39
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def getStockCodeDataFrame() -> pd.core.frame.DataFrame:

    URL = 'https://www.jpx.co.jp/markets/statistics-equities/misc/01.html'


    response = urllib.request.urlopen(URL).read().decode("utf-8")
    string_html = re.findall('<a href=\".+?\.xls\"',response)
    url_list = []
    for i in string_html:
        j = i.lstrip('<a href=\"')
        k = j.rstrip('\"')
        url_list.append('https://www.jpx.co.jp'+k)
    url = url_list[0]

    #国内株式のみ抽出

    df = pd.read_excel(url)
    df = df[(df.iloc[:,3] == 'プライム（内国株式）' ) | (df.iloc[:,3] == 'スタンダード（内国株式）' ) | (df.iloc[:,3] == 'グロース（内国株式）' ) ]

    #列名の変更
    df.columns = ['date', 'code', 'office_name', 'market_class', 'industry_detail_code', 'industry_detail', 'industry_code', 'industry','scale_code','scale_class']

    #'date'列をdatetime->strへ型変換
    df['date'] = df['date'].astype(str)
    df['code'] = df['code'].astype(str)
    df['industry_detail_code'] = df['industry_detail_code'].astype(str)
    df['industry_code'] = df['industry_code'].astype(str)
    df['scale_code'] = df['scale_code'].astype(str)

    return df