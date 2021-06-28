from lxml import etree
import requests
from bs4 import BeautifulSoup
import re
import numpy as np
from bs4 import NavigableString
import random

headers = {
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.2.28) Gecko/20120306 Firefox/3.6.28",
    "Mozilla/5.0 (Windows NT 5.1; rv:2.0) Gecko/20100101 Firefox/4.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:10.0.8) Gecko/20100101 Firefox/10.0.8",
    "Mozilla/5.0 (Windows NT 6.1; rv:17.0) Gecko/20100101 Firefox/17.0 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:20.0) Gecko/20100101 Firefox/20.0",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.33 Safari/535.11",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.142 Safari/535.19",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.64 Safari/537.31",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Maxthon)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Maxthon 2.0)",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/3.0 Chrome/22.0.1229.79 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.5.4000 Chrome/26.0.1410.43 Safari/537.1",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; qihu theworld)",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.79 Safari/535.11 QIHU THEWORLD",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; TencentTraveler )",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.7 (KHTML, like Gecko) Chrome/20.0.1099.0 Safari/536.7 QQBrowser/6.14.15493.201",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.3.8581.400) ",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.802.30 Safari/535.1 SE 2.X MetaSr 1.0",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17 SE 2.X MetaSr 1.0",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER",
    "Opera/9.80 (Windows NT 6.1) Presto/2.12.388 Version/12.15",
    "Opera/9.80 (X11; Linux x86_64) Presto/2.12.388 Version/12.15",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0),",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322),",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30),",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30),",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6,",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1,",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0,",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 SE 2.X MetaSr 1.0",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E) QQBrowser/6.9.11079.201",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
    "User-Agent,Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "User-Agent,Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "User-Agent,Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
    "User-Agent,Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "User-Agent,Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "User-Agent, Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1",
    "User-Agent,Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1",
    "User-Agent,Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "User-Agent,Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "User-Agent, Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "User-Agent, Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "User-Agent, Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "User-Agent, Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "User-Agent, Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "User-Agent, Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "User-Agent, Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "User-Agent, Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "User-Agent,Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36",
    "User-Agent,Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "User-Agent,Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "User-Agent,Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "User-Agent, Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "User-Agent, MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "User-Agent, Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "User-Agent, Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "User-Agent, Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "User-Agent, Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "User-Agent, Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "User-Agent, Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "User-Agent, UCWEB7.0.2.37/28/999",
    "User-Agent, NOKIA5700/ UCWEB7.0.2.37/28/999",
    "User-Agent, Openwave/ UCWEB7.0.2.37/28/999",
    "User-Agent, Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 5.2)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)",
    "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv 11.0) like Gecko",
    "User-Agent : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36Edge/13.10586",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0; LG; GW910)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; SAMSUNG; SGH-i917)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 920)",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_4 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) CriOS/27.0.1453.10 Mobile/10B350 Safari/8536.25",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko)Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19",
    "Mozilla/5.0 (Linux; Android 4.1.2; Nexus 7 Build/JZ054K) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
    "Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3",
    "Mozilla/5.0 (iPad; CPU OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B466 Safari/600.1.4",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A366 Safari/600.1.4",
    "Mozilla/5.0 (iPod; CPU iPhone OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3",
    "Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0",
    "Mozilla/5.0 (Linux; Android 4.1.2; Nexus 7 Build/JZ054K) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20130331 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.9.168 Version/11.52",
    "Opera/9.80 (Windows NT 6.1; WOW64; U; en) Presto/2.10.229 Version/11.62",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.18 Safari/537.36 Edg/75.0.139.4",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
    "Mozilla/5.0 (Linux; Android 9; BKL-AL20 Build/HUAWEIBKL-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Mobile Safari/537.36 EdgA/42.0.0.2741"
}
def get_urlnum(furl,headers):
    tmp_head = random.choice(list(headers))
    tmp_head = str(tmp_head)

    r = requests.get(furl, headers={'User-Agent':tmp_head}, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    content = r.content
    soup = BeautifulSoup(content,features="lxml")
    frist_data = soup.find('a',{'href':"javascript:void 0"})
    my_list = []
    for one in frist_data.parent.parent.parent:
        a = one.parent.find_all('td',class_="wh-10 b-l")
        my_list.append(a)
    c = my_list[0]
    my_num_list = []
    for num in range(0,len(c)):
        d = c[num].attrs
        my_num = d.get('newplayid')
        my_num_list.append(my_num)
    return my_num_list
def get_web(url,headers):
    tmp_head = random.choice(list(headers))
    tmp_head = str(tmp_head)

    try:
        r = requests.get(url, headers={'User-Agent':tmp_head}, timeout=30)
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
    host_num = html.find('div',{'class':"team-add-info-zd"}).get_text()
    visit_num = html.find('div',{'class':"team-add-info-kd"}).get_text()
    host_info = html.find('div',{'class':"team-info-h"}).get_text().replace(' ','').replace('\r','').replace('\n','').replace('\t','')
    visit_info = html.find('div',{'class':"team-info-v"}).get_text().replace(' ','').replace('\r','').replace('\n','').replace('\t','')

    host_p = html.find('span',{'class':"h-s"})
    visit_p = html.find('span',{'class':"v-s"})
    second_data = host_name.get_text().replace(' ','').replace('\r','').replace('\n','').replace('\t','')
    third_data = visit_name.get_text().replace(' ','').replace('\r','').replace('\n','').replace('\t','')
    if host_p is not None:
        host_p =host_p.get_text().replace(' ','')
        visit_p = visit_p.get_text().replace(' ','')
    return second_data, host_p, visit_p, third_data
def get_teaminfo(html):
    frist_data = html.title.string[0:-6]
    # 找到赔率表的内容
    host_info = html.find('div',{'class':"team-info-h"}).get_text().replace(' ','').replace('\r','').replace('\n','').replace('\t','')
    visit_info = html.find('div',{'class':"team-info-v"}).get_text().replace(' ','').replace('\r','').replace('\n','').replace('\t','')
    return host_info,visit_info
def get_teamnum(html):
    frist_data = html.title.string[0:-6]
    host_num = html.find('div',{'class':"team-add-info-zd"}).get_text()
    visit_num = html.find('div',{'class':"team-add-info-kd"}).get_text()
    host_num = int(host_num[-2:].replace('：',''))
    visit_num = int(visit_num[-2:].replace('：',''))
    if host_num-visit_num < 0:
        print('预测结果可以买','\t','3')
    elif host_num-visit_num >0:
        print('预测结果可以买','\t','0')
    else:
        print('预测结果可以买','\t','1')
    return host_num,visit_num

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
def asia(url,headers,html,result,mydata):
    url = url[0:-4]
    url = url+'ypdb'
    tmp_head = random.choice(list(headers))
    tmp_head = str(tmp_head)
    r = requests.get(url, headers={'User-Agent':tmp_head}, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    content = r.content
    soup = BeautifulSoup(content,features="lxml")
    for i in range(3,18):
        betname = soup.find_all('tr')[i].find_all('td')[1]
        host_first = soup.find_all('tr')[i].find_all('td')[2]
        ball = soup.find_all('tr')[i].find_all('td')[3]
        visit_first = soup.find_all('tr')[i].find_all('td')[4]
        ball1 = soup.find_all('tr')[i].find_all('td')[6]
        if betname and host_first and ball and visit_first is not None:
            betname = betname.get_text()
            host_first = host_first.get_text()
            ball = ball.get_text()
            visit_first = visit_first.get_text()
        if betname == 'Interwetten':
            aa = float(host_first)
            aaa = float(visit_first)
        if betname == '18Bet':
            bb = float(host_first)
            bbb = float(visit_first)
#            print(get_gameinfo(html))
#            print(get_teamnum(html))
#            print(get_teaminfo(html))
            if (aa < aaa and bb < bbb) or (aa > aaa and bb > bbb):
                print('same as give')
                print(get_gameinfo(html))
                print(get_teaminfo(html))
                print(aa,ball,aaa)
                print(bb,ball,bbb)
                print(get_teamnum(html))
            else:
                print('not same as give')
            if aa - 0.75 == 0 or aaa - 0.75 == 0: 
                print(get_gameinfo(html))
                print(get_teaminfo(html))
                print('may be 1')
    #for i in range(3,18):
    #    identity = 'bold-g'
    #    host_first_iden = soup.find_all('tr')[i].find_all('td')[2]['class']
    #    if identity in host_first_iden:
    #        betname = soup.find_all('tr')[i].find_all('td')[1].get_text()
    #        host_first = soup.find_all('tr')[i].find_all('td')[2]['data']
    #        ball = soup.find_all('tr')[i].find_all('td')[3]['data']
    #        visit_first = soup.find_all('tr')[i].find_all('td')[4]['data']
    #        host_last = soup.find_all('tr')[i].find_all('td')[5]['data']
    #        ball1 = soup.find_all('tr')[i].find_all('td')[6]['data']
    #        visit_last = soup.find_all('tr')[i].find_all('td')[7]['data']
    #        if betname == 'Interwetten' and float(host_first) <= 0.70 :
    #            #print(get_gameinfo(html))
    #            #print(get_teamnum(html))
    #            #print(get_teaminfo(html))
    #            #print('预测结果可以买','\t',judge(result,mydata))
    #            #fangcha(url,headers)
    #            print(betname,host_first,ball,visit_first,'\t',host_last,ball1,visit_last)
    #            break
    #for j in range(3,18):
    #    identity = 'bold-g'
    #    visit_first_iden = soup.find_all('tr')[j].find_all('td')[4]['class']
    #    if identity in visit_first_iden:
    #        betname = soup.find_all('tr')[j].find_all('td')[1].get_text()
    #        host_first = soup.find_all('tr')[j].find_all('td')[2]['data']
    #        ball = soup.find_all('tr')[j].find_all('td')[3]['data']
    #        visit_first = soup.find_all('tr')[j].find_all('td')[4]['data']
    #        host_last = soup.find_all('tr')[i].find_all('td')[5].get_text()
    #        ball1 = soup.find_all('tr')[i].find_all('td')[6].get_text()
    #        visit_last = soup.find_all('tr')[i].find_all('td')[7].get_text()
    #        if betname == 'Interwetten' and float(visit_first) < 0.70 :
    #            #print(get_gameinfo(html))
    #            #print(get_teamnum(html))
    #            #print(get_teaminfo(html))
    #            #print('预测结果可以买','\t',judge(result,mydata))
    #            #fangcha(url,headers)
    #            print(betname,host_first,ball,visit_first,'\t',host_last,ball1,visit_last)
    #            break
def fangcha(url,headers):
    url = url[0:-4]
    url = url+'bfyc'
    tmp_head = random.choice(list(headers))
    tmp_head = str(tmp_head)
    r = requests.get(url, headers={'User-Agent':tmp_head}, timeout=30)
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
def game_start(num):
    global headers 
    url = 'https://fenxi.zgzcw.com/%s/bjop'%num
    html = get_web(url,headers)
    mydata = get_mydata(html)
    result = analisys_data(mydata)
    #print(get_gameinfo(html))
    #print(get_teamnum(html))
    #print(get_teaminfo(html)) 
    #print('+++++++++++++++++++++++++++')
    #print('预测结果可以买','\t',judge(result,mydata))
    #fangcha(url,headers)
    asia(url,headers,html,result,mydata)
    print('----------------------------------------------------------')
if __name__ == '__main__':
    address = input('url:')
    furl = address
    get_urlnum(furl,headers)
    for i in get_urlnum(furl,headers):
        game_start(i)
