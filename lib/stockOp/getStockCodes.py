import pandas as pd
import re
import urllib.request
import tabula

#セキュリティ的にだめ！！（一時凌ぎ）
#https://qiita.com/shutokawabata0723/items/9733a7e640a175c23f39
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def getStockCodeDataFrame() -> pd.core.frame.DataFrame:
    
    '''
    東証の上場銘柄コード一覧をdf形式で出力する。
    URL = 'https://www.jpx.co.jp/markets/statistics-equities/misc/01.html'
    '''

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

def getCreditBalancesInfo(date_go:int) -> pd.core.frame.DataFrame:
    '''
    全銘柄の信用残高一覧を保持する。

    date_go は信用残高一覧が5日分のデータを保持している。
        1:直近版
        2:前回版
        ...
        5:一番古い
       
    URL = 'https://www.jpx.co.jp/markets/statistics-equities/margin/05.html'
    '''

    cols = ['code', 'buy_balance','sell_balance']
    df_summry = pd.DataFrame(index = [],columns = cols)

    #対象のURLより、信用残高一覧ファイルのURLを取得する。

    URL = 'https://www.jpx.co.jp/markets/statistics-equities/margin/05.html'


    response = urllib.request.urlopen(URL).read().decode("utf-8")
    string_html = re.findall('<a href=\".+?\.pdf\"',response)
    url_list = []
    for i in string_html:
        j = i.lstrip('<a href=\"')
        k = j.rstrip('\"')
        url_list.append('https://www.jpx.co.jp'+k)


    url_list.sort()
    url = url_list[-date_go]
    #-1の要素が直近版である！

    dfs_list = tabula.read_pdf(url, stream=True,pages='all',lattice=True)

    for index_dfs_list,dfs in enumerate(dfs_list): #◯ページ目のPDFデータがlist構造で格納されている。

        for index_df,df in dfs.iterrows():

            try:

                ##7532はバグで『7普53通20』ってなっているので、、
                
                sc = str(df.iloc[0])
                stockCode = sc.replace('普','')
                stockCode = stockCode.replace('通','')

                ##mmmm0の0を取り除く                    
                stockCode = str(stockCode[-5:-1])
            
                sellBalance = int(re.sub(',','',df.iloc[2]))
                buyBalance = int(re.sub(',','',df.iloc[4]))

                df_tmp = pd.DataFrame([[stockCode,buyBalance,sellBalance]],index = [stockCode],columns = cols)
                df_summry = pd.concat([df_summry,df_tmp],axis=0)

            except:
                #本当はerror関数を作ってerror通知関数を置きたい。
                continue

    #df_summryのindex=直近の銘柄コード一覧　の共通銘柄コードを抽出する。

    codes = getStockCodeDataFrame()
    merge_index_list = set(df_summry.index.to_list()) & set(codes['code'].to_list())
    merge_index = pd.Index(merge_index_list)
    df_summry = df_summry.loc[merge_index]
    
    #日付とindexを列に付与する。
    date = url[-14:-6]
    df_summry.insert(1,'date',date)

    #優先株削除処理。2593（伊藤園）などが対象となる。
    df_summry = df_summry[(~df_summry.index.duplicated(keep='first'))]
    
    return df_summry

if __name__ == '__main__':
    
    df = getCreditBalancesInfo(5)
    print(df[df['code'] =='2593'])
    
    
