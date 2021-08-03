import numpy as np
import pandas as pd
import tushare as ts
import matplotlib.pyplot as plt

def get_stock(num,start_date):
    pro = ts.pro_api('8a7c7d88f487915b8955e5b0fc6afb267029b40bdeaa90f7d37ded72')
    stock_data = pro.daily(ts_code=num, start_date=start_date, end_date='20210730')
    stock_data.to_csv('/home/yg/mydata/stock/data/{}.csv'.format(num))
    df = pd.read_csv('/home/yg/mydata/stock/data/{}.csv'.format(num),index_col = 'trade_date',parse_dates=['trade_date'])
    df = df[['open','close','high','low','vol']]
    return df
def judge(df,start_date):
    df.sort_values('trade_date',inplace=True)
    print(df)
    monthly = df.resample('M').first()
    yearly = df.resample('A').last()[:-1]
    cost_money = 0
    handle = 0
    total = 0
    for year in range(int(start_date),2021):
        cost_money += monthly.loc[str(year)]['open'].sum()*100
        handle += len(monthly.loc[str(year)]['open'])*100
        cost_money -= yearly.loc[str(year)]['open'][0]*handle
        total -= yearly.loc[str(year)]['open'][0]*handle
        handle = 0
        print(round(-cost_money,2))
        cost_money = 0
    print(round(-total,2))

if __name__ == '__main__':
    input_data = input('StockCode please:')
    num = str(input_data)
    start_date = input('start_date:')
    df = get_stock(num,start_date)
    judge(df,start_date)
