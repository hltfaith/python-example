
# 保留两位小数

a = 1
b = 3

#方法一：
print(round(a/b,2))

#方法二：
print(format(float(a)/float(b),'.2f'))

#方法三：
print ('%.2f' %(a/b))
