#!/usr/bin/env python
# coding=utf-8
import requests
def getstock(stock):
    r = requests.get("http://data.gtimg.cn/flashdata/hushen/latest/daily/{}.js?maxage=43201&visitDstTime=1".format(stock))
    with open("tmp","w") as f:
        f.write(r.text)
    datas = []
    with open("tmp") as f:
        for line in f:
            datas.append(line.strip())

    datas = datas[-4:-1]
    data = [d.split(" ") for d in datas]
    '''
    时间        今开      收盘      最高     最低    成交量
    '181218', '26.23', '25.50', '26.39', '25.34', '413674
    '''

    if float(data[-1][2]) > float(data[-2][2]) > float(data[-3][2]):
        print("收盘价走势")
        print(stock)
        print(data)

    if float(data[-1][3]) > float(data[-2][3]) > float(data[-3][3]):
        print("最高点走势")
        print(stock)
        print(data)

    if float(data[-1][-1].strip("\\n\\")) > float(data[-2][-1].strip("\\n\\")) > float(data[-3][-1].strip("\\n\\")):
        print("成交量走势")
        print(stock)
        print(data)

if __name__ == "__main__":
    stocks = []
    with open("stocks") as f:
        for line in f:
            stocks.append(line.strip())
    for s in stocks:
        getstock(s)
