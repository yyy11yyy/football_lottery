# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 16:43:14 2021

@author: YG
"""
import re

def get_row(source):
    p = re.split(r'\t',source)
    mydata_list = []
    for i in p:
        m = re.findall(r'\d+.\d+',i)
        mydata_list.append(m)
    return mydata_list
def get_first(k):
    zhusheng = float(k[0])
    ping = float(k[1])
    fu = float(k[2])
    total = zhusheng + ping + fu
    z3 = zhusheng / total
    p1 = ping / total
    f0 = fu / total
    return zhusheng,ping,fu,total,z3,p1,f0
def get_second(h):
    zhusheng1 = float(h[0])
    ping1 = float(h[1])
    fu1 = float(h[2])
    total1 = zhusheng1 + ping1 + fu1
    z13 = zhusheng1 / total1
    p11 = ping1 / total1
    f10 = fu1 / total1
    return zhusheng1, ping1, fu1, total1, z13, p11, f10
def ration(content):
    a = re.findall(r'([\d]+){0,1}胜',content)
    b = re.findall(r'([\d]+){0,1}平',content)
    c = re.findall(r'([\d]+){0,1}负',content)
    totala = 0
    totalb = 0
    totalc = 0
    for i in range(0,len(a)):
        totala = totala + int(a[i])
    for i in range(0,len(b)):
        totalb = totalb + int(b[i])
    for i in range(0,len(c)):
        totalc = totalc + int(c[i])
    total = totala+totalb+totalc
    sl = round(totala/total,2)
    pl = round(totalb/total,2)
    fl = round(totalc/total,2)
    print('胜:{}\t平{}\t负{}'.format(sl,pl,fl))
    if sl >= 0.5:
        print('3')
    elif 0.41<= sl <0.5:
        print('may be 3')
    elif pl >= 0.35:
        print('1')
    elif fl >= 0.46:
        print('0')
    elif sl >0.3 and pl>0.3 and fl >0.3:
        print('势均力敌！')
    else:
        print('不是正路！')

if __name__ == '__main__':
    while True:
        content = input('胜率'+'\n')
        print('-----------------------------------------------------------------')
        source = input('赔率'+'\n')
        print('-----------------------------------------------------------------')
        my_date = get_row(source)
        k = my_date[2]
        h = my_date[3]
        my_chu = get_first(k)
        my_zhong = get_second(h)
        ration(content)
        print('-----------------------------------------------------------------')
        print('初赔：',round(my_chu[3],3), '\n', '主胜', round(my_chu[4], 3), '平', round(my_chu[5], 3), '客胜', round(my_chu[6], 3))
        print('终赔：', round(my_zhong[3],3), '\n', '主胜', round(my_zhong[4], 3), '平', round(my_zhong[5], 3), '客胜', round(my_zhong[6], 3))
        if (round(my_chu[4], 3) - round(my_zhong[4], 3)) > 0 and round(my_zhong[4],3) <= 0.056:
            print('考虑3')
        elif (round(my_chu[6],3) - round(my_zhong[6], 3)) > 0 and round(my_zhong[6],3) <= 0.071:
            print('考虑0')
        elif (round(my_chu[5],3) - round(my_zhong[5], 3)) > 0 and round(my_zhong[5],3) <= 0.2:
            print('考虑1')
        else:
            print('考虑被让球方 胜平 ')
