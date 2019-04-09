
# BeautifulSoup库的使用

'''

上一篇文章的正则，其实对很多人来说用起来是不方便的，加上需要记很多规则，所以用起来不是特别熟练，
而这节我们提到的beautifulsoup就是一个非常强大的工具，爬虫利器。

beautifulSoup “美味的汤，绿色的浓汤”

一个灵活又方便的网页解析库，处理高效，支持多种解析器。
利用它就不用编写正则表达式也能方便的实现网页信息的抓取

'''

from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''

# soup = BeautifulSoup(html, 'lxml')

# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)

# print(soup.p)
# print(soup.p['class'])
# print(soup.a)

# print(soup.find_all('a'))
# print(soup.find(id='link3'))


# 可以分别获取所有的链接，以及文字内容
# for link in soup.find_all('a'):
#     print(link.get('href'))
#
# print(soup.get_text())


'''

解析器

Beautiful Soup支持Python标准库中的HTML解析器,还支持一些第三方的解析器，如果我们不安装它，
则 Python 会使用 Python默认的解析器，lxml 解析器更加强大，速度更快，推荐安装。


基本使用
标签选择器

在快速使用中我们添加如下代码：
print(soup.title)
print(type(soup.title))
print(soup.head)
print(soup.p)

通过这种soup.标签名 我们就可以获得这个标签的内容
这里有个问题需要注意，通过这种方式获取标签，如果文档中有多个这样的标签，返回的结果是第一个标签的内容，
如上面我们通过soup.p获取p标签，而文档中有多个p标签，但是只返回了第一个p标签内容

获取名称
当我们通过soup.title.name的时候就可以获得该title标签的名称，即title

获取属性
print(soup.p.attrs['name'])
print(soup.p['name'])
上面两种方式都可以获取p标签的name属性值

获取内容
print(soup.p.string)
结果就可以获取第一个p标签的内容：
The Dormouse's story

嵌套选择

我们直接可以通过下面嵌套的方式获取
print(soup.head.title.string)




'''

# 子节点和子孙节点
# contents的使用

html2 = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

# soup = BeautifulSoup(html2, 'lxml')
# print(soup.p.contents)

# 结果是将p标签下的所有子标签存入到了一个列表中


'''

children的使用

通过下面的方式也可以获取p标签下的所有子节点内容和通过contents获取的结果是一样的，
但是不同的地方是soup.p.children是一个迭代对象，而不是列表，只能通过循环的方式获取素有的信息

'''
#
# print(soup.p.children)
# for i,child in enumerate(soup.p.children):
#     print(i,child)
#
# 通过contents以及children都是获取子节点，如果想要获取子孙节点可以通过descendants
# print(soup.descendants)同时这种获取的结果也是一个迭代器


'''

父节点和祖先节点

通过soup.a.parent就可以获取父节点的信息

通过list(enumerate(soup.a.parents))可以获取祖先节点，这个方法返回的结果是一个列表，
会分别将a标签的父节点的信息存放到列表中，以及父节点的父节点也放到列表中，并且最后还会讲整个文档放到列表中，
所有列表的最后一个元素以及倒数第二个元素都是存的整个文档的信息

兄弟节点

soup.a.next_siblings 获取后面的兄弟节点
soup.a.previous_siblings 获取前面的兄弟节点
soup.a.next_sibling 获取下一个兄弟标签
souo.a.previous_sinbling 获取上一个兄弟标签

'''


'''

标准选择器
find_all
find_all(name,attrs,recursive,text,**kwargs)
可以根据标签名，属性，内容查找文档

'''

html3 = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

# soup = BeautifulSoup(html3, 'lxml')

# name的用法
# print(soup.find_all('ul'))
# print(type(soup.find_all('ul')[0]))

# 同时我们是可以针对结果再次find_all,从而获取所有的li标签信息
# for ul in soup.find_all('ul'):
#     print(ul.find_all('li'))



# attrs 参数使用方法

'''
attrs可以传入字典的方式来查找标签，但是这里有个特殊的就是class,因为class在python中是特殊的字段，
所以如果想要查找class相关的可以更改attrs={'class_':'element'}或者soup.find_all('',{"class":"element})，
特殊的标签属性可以不写attrs，例如id

'''


html4 = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

# soup = BeautifulSoup(html4, 'lxml')
# print(soup.find_all(attrs={'id': 'list-1'}))
# print(soup.find_all(attrs={'name': 'elements'}))


# text 参数使用方法
'''
    结果返回的是查到的所有的text='Foo'的文本
'''

html5='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

# soup = BeautifulSoup(html5, 'lxml')
# print(soup.find_all(text='Foo'))


'''

find
find(name,attrs,recursive,text,**kwargs)
find返回的匹配结果的第一个元素

其他一些类似的用法：
find_parents()返回所有祖先节点，find_parent()返回直接父节点。
find_next_siblings()返回后面所有兄弟节点，find_next_sibling()返回后面第一个兄弟节点。
find_previous_siblings()返回前面所有兄弟节点，find_previous_sibling()返回前面第一个兄弟节点。
find_all_next()返回节点后所有符合条件的节点, find_next()返回第一个符合条件的节点
find_all_previous()返回节点后所有符合条件的节点, find_previous()返回第一个符合条件的节点


'''


'''

CSS选择器
通过select()直接传入CSS选择器就可以完成选择
熟悉前端的人对CSS可能更加了解，其实用法也是一样的
.表示class #表示id
标签1，标签2 找到所有的标签1和标签2
标签1 标签2 找到标签1内部的所有的标签2
[attr] 可以通过这种方法找到具有某个属性的所有标签
[atrr=value] 例子[target=_blank]表示查找所有target=_blank的标签

'''

html6 = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
# soup = BeautifulSoup(html6, 'lxml')
# print(soup.select('.panel .panel-heading'))
# print(soup.select('ul li'))
# print(soup.select('#list-2 .element'))
# print(type(soup.select('ul')[0]))



'''

获取内容

通过get_text()就可以获取文本内容

'''

html7 = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

# soup = BeautifulSoup(html7, 'lxml')
# for li in soup.select('li'):
#     print(li.get_text)



'''

获取属性
或者属性的时候可以通过[属性名]或者attrs[属性名]

'''

html8='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

soup = BeautifulSoup(html8, 'lxml')
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])



'''

总结
推荐使用lxml解析库，必要时使用html.parser
标签选择筛选功能弱但是速度快
建议使用find()、find_all() 查询匹配单个结果或者多个结果
如果对CSS选择器熟悉建议使用select()
记住常用的获取属性和文本值的方法

'''

