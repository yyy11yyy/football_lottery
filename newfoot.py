# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 16:14:18 2021

@author: YG
"""
import re
def get_row(row_data):
    first_list = []
    for i in row_data.split('\t'):
        first_list.append(i)
    second_list = []
    for j in range(0, 2):
        second_list.append(first_list[j].split())
    return second_list
def get_first(second_list):
    for k in second_list:
        zhusheng = float(k[0])
        ping = float(k[1])
        fu = float(k[2])
        total = zhusheng + ping + fu
        z3 = zhusheng / total
        p1 = ping / total
        f0 = fu / total
        break
    return zhusheng,ping,fu,total,z3,p1,f0
def get_second(second_list):
    for h in second_list:
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
if __name__ == '__main__':
#    row_datalist = []
#    flag = True
#    while flag:
#        judge = input()
#        if judge == '111':
#            flag = False
#        if judge != '111':
#            row_data = judge
#            row_datalist.append(row_data)
#    for row in row_datalist:
    content = input('胜率')
    row = input('赔率')
    print('-----------------------------------------------------------------')
    my_date = get_row(row)
    my_chu = get_first(my_date)
    my_zhong = get_second(my_date)
    ration(content)
    print('----------------------------------------------------------------------------------------------')
    print('初赔：',round(my_chu[3],3), '\n', '主胜', round(my_chu[4], 3), '平', round(my_chu[5], 3), '客胜', round(my_chu[6], 3))
    print('终赔：', round(my_zhong[3],3), '\n', '主胜', round(my_zhong[4], 3), '平', round(my_zhong[5], 3), '客胜', round(my_zhong[6], 3))
    if (round(my_chu[4], 3) - round(my_zhong[4], 3)) > 0 and round(my_zhong[4],3) <= 0.056:
        print('考虑3')
    elif (round(my_chu[6],3) - round(my_zhong[6], 3)) > 0 and round(my_zhong[6],3) <= 0.071:
        print('考虑0')
    elif (round(my_chu[5],3) - round(my_zhong[5], 3)) > 0 and round(my_zhong[5],3) <= 0.28:
        print('考虑1')
    else:
        print('考虑被让球方 胜平 ')
