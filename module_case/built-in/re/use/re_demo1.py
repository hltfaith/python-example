
'''

正则表达式是对字符串操作的一种逻辑公式，就是 事先定义好的一些特定字符、及这些特定字符的组合，
组成一个“规则字符”，这个“规则字符” 来表达对字符的一种过滤逻辑。

正则并不是python独有的，其他语言也都有正则
python中的正则，封装了re模块

'''


'''
常用的匹配模式

\w      匹配字母数字及下划线
\W      匹配f非字母数字下划线
\s      匹配任意空白字符，等价于[\t\n\r\f]
\S      匹配任意非空字符
\d      匹配任意数字
\D      匹配任意非数字
\A      匹配字符串开始
\Z      匹配字符串结束，如果存在换行，只匹配换行前的结束字符串
\z      匹配字符串结束
\G      匹配最后匹配完成的位置
\n      匹配一个换行符
\t      匹配一个制表符
^       匹配字符串的开头
$       匹配字符串的末尾
.       匹配任意字符，除了换行符，re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符
[....]  用来表示一组字符，单独列出：[amk]匹配a,m或k
[^...]  不在[]中的字符：[^abc]匹配除了a,b,c之外的字符
*       匹配0个或多个的表达式
+       匹配1个或者多个的表达式
?       匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
{n}     精确匹配n前面的表示
{m,m}   匹配n到m次由前面的正则表达式定义片段，贪婪模式
a|b     匹配a或者b
()      匹配括号内的表达式，也表示一个组

'''


'''
# re.match()
# 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配的话，match（）就会返回None
# 最常规的匹配
import re

content= "hello 123 4567 World_This is a regex Demo"
result = re.match('^hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$',content)
print(result)
print(result.group())
print(result.span())

# result.group()获取匹配的结果
# result.span()获去匹配字符串的长度范围
'''

'''
# 泛匹配
import re

content= "hello 123 4567 World_This is a regex Demo"
result = re.match("^hello.*Demo$", content)
print(result)
print(result.group())
print(result.span())
'''


'''
# 匹配目标
# 如果为了匹配字符串中具体的目标，则需要通过（）括起来，例子如下：
import re
content= "hello 1234567 World_This is a regex Demo"
result = re.match('^hello\s(\d+)\sWorld.*Demo$',content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())

'''


'''
# 匹配模式
# 很多时候匹配的内容是存在换行的问题的，这个时候的就需要用到匹配模式re.S来匹配换行的内容
import re


content = """hello 123456 world_this
my name is zhaofan
"""

result =re.match('^he.*?(\d+).*?zhaofan$',content,re.S)
print(result)
print(result.group())
print(result.group(1))
'''


'''
# 转义
# 当我们要匹配的内容中存在特殊字符的时候，就需要用到转移符号\,例子如下：
import re

content= "price is $5.00"

result = re.match('price is \$5\.00',content)
print(result)
print(result.group())
'''


'''
# re.search
# re.search扫描整个字符串返回第一个成功匹配的结果

import re

content = "extra things hello 123455 world_this is a Re Extra things"

result = re.search("hello.*?(\d+).*?Re",content)
print(result)
print(result.group())
print(result.group(1))
'''


# 匹配演练
import re

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''

'''
result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
print(result)
print(result.groups())
print(result.group(1))
print(result.group(2))


'''

# re.findall
# 搜索字符串，以列表的形式返回全部能匹配的子串

html1 = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''

'''
results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html1, re.S)
print(results)
print(type(results))
for result in results:
    print(result)
    print(result[0], result[1], result[2])


'''


import re

html2 = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''
'''
results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>',html2,re.S)
print(results)
for result in results:
    print(result[1])

'''


# re.sub
# 替换字符串中每一个匹配的子串后返回替换后的字符串
#
# re.sub(正则表达式，替换成的字符串，原字符串)

# content = "Extra things hello 123455 World_this is a regex Demo extra things"
#
# content = re.sub('\d+','',content)
# print(content)

