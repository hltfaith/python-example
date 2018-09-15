from tools.export_xslx import xslx_data
from asset.models import asset_db
import time

# print(xslx_data())

data = xslx_data()

print(type(data))

lst2 = list(data.values())
#print(lst2)
# for i in lst2:
#     print(i)


count = 0
for i in data:
    count += 1

# 格式
# [['1',2,3], [1,2,3]]

num_list = []

# 字典遍历出来,写入数据库
for i in data:

    val = data[i].strip('[]')
    val = str(val).split(",")

   # print(eval(val[0]))
    asset_db.objects.create(hostname=eval(val[0]), ip_addr=eval(val[1]), username=eval(val[2]), password=eval(val[3]),
                            model=eval(val[4]), sn=eval(val[5]), local=eval(val[6]), resource_type=eval(val[7]), port=eval(val[8]),
                            system_version=eval(val[9]), group=eval(val[10])
                            )



    # for k in val:
    #     b = eval(k)
    #     num_list.append(b)




    # for num in num_list:
    #     print(num)

    #print(num_list)
    # a = num_list[0].strip('[]').split(',')
    # print(a)

        # print(num_list[k])
        # a = num_list[0].strip('[]').split(',')

# print(count)
#
# print(num_list)
#print(a[0])
#print(a[0])
#resource_db.objects.create(title=title,price=price,pub_date=date,publish=publish)


