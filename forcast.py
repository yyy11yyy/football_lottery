from lxml import etree
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re
import numpy as np
from bs4 import NavigableString

def get_web(url):
    ua = UserAgent()
    headers = {"User-Agent": ua.random}
    try:
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        # 如果状态不是200，引发HTMLError异常
        r.encoding = r.apparent_encoding
        content = r.content
    except:
        print("产生异常")

    soup = BeautifulSoup(content,features="lxml")
    return soup
def get_gameinfo(html):
    # 比赛场次介绍
    frist_data = html.title.string[0:-6]
    # 找到赔率表的内容
    host_name = html.find('div',{'class':"host-name"})
    visit_name = html.find('div',{'class':"visit-name"})
    host_p = html.find('span',{'class':"h-s"})
    visit_p = html.find('span',{'class':"v-s"})
    second_data = host_name.get_text().replace(' ','').replace('\r','').replace('\n','').replace('\t','')
    third_data = visit_name.get_text().replace(' ','').replace('\r','').replace('\n','').replace('\t','')
    return second_data, host_p, visit_p, third_data
def get_mydata(html):
    # 比赛场次介绍
    frist_data = html.title.string[0:-6]
    # 找到赔率表的内容
    frist_data = html.find('div',{'id':"data-body",})
    # second_data = frist_data.get_text().replace(' ','').replace('\r','').replace('\n','').split('\t'*14)
    second_data = frist_data.get_text().replace(' ','').replace('\r','').replace('主客同','').replace('\n'*2,'').split('\t'*14)
    second_data = second_data[1:]
    my_data = []
    for a in second_data:
        data = a.split('\n')[0:5]
        my_data.append(data)
    return my_data
def analisys_data(my_data):
    new_data = []
    host_data = []
    equal_data = []
    guest_data = []
    for first_round in my_data:
        id = first_round[0]
        name = first_round[1]
        host = first_round[2]
        equal = first_round[3]
        guest = first_round[4]
        data = name, float(host), float(equal), float(guest)
        new_data.append(data)
        host_data.append(float(host))
        equal_data.append(float(equal))
        guest_data.append(float(guest))
    host = np.min(host_data)
    equal = np.min(equal_data)
    guest = np.min(guest_data)
    result = []
    for h in new_data:
        if host == h[1]:
            result.append(h)
    for e in new_data:
        if equal == e[2]:
            result.append(e)
    for g in new_data:
        if guest == g[3]:
            result.append(g)
    return result
def asia(url):
    url = url[0:-4]
    url = url+'ypdb'
    ua = UserAgent()
    headers = {"User-Agent": ua.random}
    r = requests.get(url, headers=headers, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    content = r.content
    soup = BeautifulSoup(content,features="lxml")
    frist_data = soup.find_all('tr')
    a = frist_data
    my_list = []
    for i in a:
        my_list.append(i)
    l = []
    for j in my_list:
        b = j.get_text()
        l.append(b)
    round_num = l[-2].replace('\n','').replace('↓','').replace('↑','').replace('主客同','')
    round_num = int(re.findall('\d+',round_num)[0])
    for i in range(3,round_num+3):
        c = l[i].replace('\n','').replace('↓','').replace('↑','').replace('主客同','')
        bet_company = re.findall('\D+',c)[0]
        first_time = re.findall('\D+',c)[2]
        last_time = re.findall('\D+',c)[5]
        print(first_time,'\t',last_time)
def fangcha(url):
    url = url[0:-4]
    url = url+'bfyc'
    ua = UserAgent()
    headers = {"User-Agent": ua.random}
    r = requests.get(url, headers=headers, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    content = r.content
    soup = BeautifulSoup(content,features="lxml")
    a = soup.find_all('div',{'class':'var-ps-2'})
    my = []

    for i in a:
        my.append(i)

    k = []
    for j in my:
        k.append(j.get_text())
    f_win = k[0]
    f_win = float(f_win[-4:])
    f_eql = k[1]
    f_eql = float(f_eql[-4:])
    f_gus = k[2]
    f_gus = float(f_gus[-4:])
    l_win = k[3]
    l_win = float(l_win[-4:])
    l_eql = k[4]
    l_eql = float(l_eql[-4:])
    l_gus = k[5]
    l_gus = float(l_gus[-4:])
    if f_win < f_eql and f_win < f_gus:
        print('variance预测结果可以买','\t','3')
        if f_win < l_win:
            print('胜没变化')
        else:
            print('胜变得更确定了')
    if f_eql < f_win and f_eql < f_gus:
        print('variance预测结果可以买','\t','1')
        if f_eql < l_eql:
            print('平没变化')
        else:
            print('平变得更确定了')

    if f_gus < f_win and f_gus < f_eql:
        print('variance预测结果可以买','\t','0')
        if f_eql < l_eql:
            print('负没变化')
        else:
            print('负变得更确定了')

def judge(result,mydata):
    print(mydata[1])
    print('************************')
    for ok in result:
        host = ok[1]
        jc_host = float(mydata[1][2])
        equal = ok[2]
        jc_equal = float(mydata[1][3])
        guest = ok[3]
        jc_guest = float(mydata[1][4])
        host_result = []
        equal_result = []
        guest_result = []

        if jc_host < jc_equal and jc_host < jc_guest:
            if host < jc_host:
                host_result.append('3')
        if jc_equal <= 3.5:
            if equal < jc_equal:
                equal_result.append('1')
        if jc_guest < jc_equal and jc_guest < jc_equal:
            if guest < jc_guest:
                guest_result.append('0')
        if len(host_result) > len(equal_result) and len(host_result) > len(guest_result):
            return 3
        if len(host_result) < len(equal_result) and len(equal_result) > len(guest_result):
            return 1
        if len(guest_result) > len(equal_result) and len(guest_result) > len(host_result):
            return 0
if __name__ == '__main__':
    while True:
        url = input('url:')
        html = get_web(url)
        mydata = get_mydata(html)
        result = analisys_data(mydata)
        print(get_gameinfo(html))
        print('+++++++++++++++++++++++++++')
        print('预测结果可以买','\t',judge(result,mydata))
        fangcha(url)
        print('+++++++++++++++++++++++++++')
        print('亚盘变化')
        asia(url)
