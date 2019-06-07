#（1）findall
import re
ret = re.findall('\d','adsf123456we7we')    #匹配字符串中是数字的字符，并将匹配值返回到列表中
print(ret)
'''结果：
['1', '2', '3', '4', '5', '6', '7']
'''

#（2）search
ret = re.search('\d','adsf123456we7we').group()     #按照表达式匹配到第一个值就返回
print(ret)
'''结果：
'''

#（3）match
ret = re.match('\w','adsf123456we7we').group()  #按照表达式匹配开头第一个值，符合的话就返回，不符合就报错
print(ret)
'''结果：
a
'''

#（4）sub
ret = re.sub('\d','*','adsf123456we7we',0)      #匹配字符串中的数字，并且替换成*号，0表示替换所有
print(ret)
'''结果：
adsf******we*we
'''

#（5）subn
ret = re.subn('\d','*','adsf123456we7we',0)     #匹配字符串中的数字，并且替换成*号，返回一个元组，存放这替换结果和替换次数
print(ret)
'''结果：
('adsf******we*we', 7)
'''

#（6）compile
obj = re.compile('\d')  #将正则表达式编译成一个正则表达式对象
ret = obj.search('ads123asd456').group()
print(ret)
'''结果：
'''

#（7）finditer
ret = re.finditer('\d','adsf451we15615adf16')   #finditer返回一个存放匹配结果的迭代器
print(ret)
for i in ret:
    print(i.group())
    
    
