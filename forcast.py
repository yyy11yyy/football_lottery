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
if __name__ == '__main__':
    total_flag = 32
    standard = 0.185
    row_datalist = []
    flag = True
    while flag:
        judge = input()
        if judge == '111':
            flag = False
        if judge != '111':
            row_data = judge
            row_datalist.append(row_data)
    for row in row_datalist:
        my_date = get_row(row)
        my_chu = get_first(my_date)
        my_zhong = get_second(my_date)
        print('----------------------------------------------------------------------------------------------')
        print('初赔：',round(my_chu[3],3), '\n', '主胜', round(my_chu[4], 3), '平', round(my_chu[5], 3), '客胜', round(my_chu[6], 3))
        print('终赔：', round(my_zhong[3],3), '\n', '主胜', round(my_zhong[4], 3), '平', round(my_zhong[5], 3), '客胜', round(my_zhong[6], 3))
        if round(my_zhong[0], 3) - round(my_chu[0], 3) < -20:
            print('主胜降盘', round((my_zhong[0] - my_chu[0]), 3),'may be 3')
        if round(my_zhong[1], 3) - round(my_chu[1], 3) < -20:
            print('平降盘', round((my_zhong[1] - my_chu[1]), 3),'may be 1')
        if round(my_zhong[2], 3) - round(my_chu[2], 3) < -20:
            print('客胜降盘', round((my_zhong[2] - my_chu[2]), 3),'may be 0')
        if round(my_zhong[0], 3) - round(my_chu[0], 3) > 10:
            print('主胜UP', round((my_zhong[0] - my_chu[0]), 3),'主胜UP客胜')
        if round(my_zhong[1], 3) - round(my_chu[1], 3) > 10:
            print('平UP', round((my_zhong[1] - my_chu[1]), 3))
        if 10 < round(my_zhong[2], 3) - round(my_chu[2], 3) < 15:
            print('客胜UP', round((my_zhong[2] - my_chu[2]), 3),'有可能大冷')
        if my_chu[3] > total_flag:
            if (my_chu[0] < my_chu[1] and my_chu[0] < my_chu[2]) and (my_zhong[0] < my_zhong[1] and my_zhong[0] < my_zhong[2]):
                if my_chu[4] < standard and 0.069<= my_chu[0] <= 0.08:
                    if my_zhong[0] / my_chu[0] > 1.5:
                        print("小心变化")
                    print(3)
                    continue
            if (my_chu[1] < my_chu[0] and my_chu[1] < my_chu[2]) and (my_zhong[1] < my_zhong[0] and my_zhong[1] < my_zhong[2]):
                if my_chu[5] < standard:
                    if my_zhong[1] / my_chu[1] > 1.5:
                        print("小心变化")
                    print(1)
                    continue
            if (my_chu[2] < my_chu[0] and my_chu[2] < my_chu[1]) and (my_zhong[2] < my_zhong[0] and my_zhong[2] < my_zhong[1]):
                if my_chu[6] < standard:
                    if my_zhong[2] / my_chu[2] > 1.5:
                        print("小心变化")
                print(0)
                continue
            else:
                print('我是因为standard')
                print("It's depend on ")
                print('如果优势方赔率为1.2，可以选低赔!')
                print('如果优势方赔率为1.4，可以选中高赔!')
                print('如果优势方赔率为1.5，可以选让球高赔和中赔!')
                print('如果优势方赔率为1.6，选高低赔')
                print('如果优势方赔率为1.7，选高低赔')
                print('如果优势方赔率为1.8，选中低赔')
                print('如果优势方赔率为1.9，选中低赔')
                print('如果优势方赔率为2，选中低赔')
        else:
            print('我是因为total')
            print('让球中低赔')

