import openpyxl
import re

wb = openpyxl.load_workbook('account.xlsx')
#print(wb.get_sheet_names())

sheet = wb.get_sheet_by_name('account')

a_list = []
for i in range(4098):
    i += 1
    ai = ('A' + str(i))
    a_list.append(ai)

h_list = []
for k in range(4098):
    k += 1
    hk = ('H' + str(k))
    h_list.append(hk)

ah_dic = {}
count = 1
while count <= 4098:
    adic = ('A' + str(count))
    hdic = ('H' + str(count))
    ah_dic[adic] = hdic
    count += 1

a_value_list = []
h_value_list = []

def jxs():
    for name in a_list:
        a_value = sheet[name].value
        match = re.search('[a-z]{10}', str(a_value))
        if match:
            a_value_list.append(a_value)
            h_value_list.append(sheet[ah_dic[name]].value)

def cydw():
    for name in a_list:
        a_value = sheet[name].value
        match = re.search('[\d]', str(a_value))
        if match:
            a_value_list.append(a_value)
            h_value_list.append(sheet[ah_dic[name]].value)

def export_xlsx():
    ws = openpyxl.Workbook()
    ws1 = ws.active
    dest_filename = 'vpnuser.xlsx'

    num1 = 1
    for name in a_value_list:
        a = ('A' + str(num1))
        ws1[a] = name
        num1 += 1

    num2 = 1
    for value in h_value_list:
        b = ('B' + str(num2))
        ws1[b] = value
        num2 += 1

    ws.save(dest_filename)
    print("VPN用户信息导出成功！！！")


if __name__ == '__main__':

    menu = ('''
    **********vpn用户授权信息自动化导出***********
        1.经销商
        2.成员单位
    ''')

    while True:
        print(menu)
        choice = int(input("请选择编号>>: ").strip())
        if choice == 1:
            jxs()
            export_xlsx()
            break

        elif choice == 2:
            cydw()
            export_xlsx()
            break

        else:
            print("输入有误！请重新输入.....")
            continue
