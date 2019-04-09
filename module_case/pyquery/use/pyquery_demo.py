
'''

PyQuery库的使用

PyQuery库也是一个非常强大又灵活的网页解析库，如果你有前端开发经验的，都应该接触过jQuery,
那么PyQuery就是你非常绝佳的选择，PyQuery 是 Python 仿照 jQuery 的严格实现。
语法与 jQuery 几乎完全相同，所以不用再去费心去记一些奇怪的方法了。

'''


'''

初始化
初始化的时候一般有三种传入方式：传入字符串，传入url,传入文件

'''

html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
</div>
'''

from pyquery import PyQuery as pq
#
# doc = pq(html)
# print(doc)
# print(type(doc))
# print(doc('li'))



# URL初始化

# doc = pq(url="http://www.baidu.com", encoding='utf-8')
# print(doc('head'))


'''

文件初始化
我们在pq()这里可以传入url参数也可以传入文件参数，当然这里的文件通常是一个html文件，例如：pq(filename='index.html')


'''


# 基本的CSS选择器

html2 = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

# doc = pq(html2)
# print(doc('#container .list li'))



'''

查找元素
子元素
children,find

'''

html3 = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

# doc = pq(html3)
# items = doc('.list')
# print(type(items))
# print(items)

# lis = items.find('li')
# print(type(lis))
# print(lis)


'''

同时在children里也可以用CSS选择器
li2 = items.children('.active') print(li2)

'''

'''

父元素
parent,parents方法
通过.parent就可以找到父元素的内容

'''

html4 = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

# doc = pq(html4)
# items = doc('.list')
# container = items.parent()
# print(type(container))
# print(container)


html5 = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''

# doc = pq(html5)
# items = doc('.list')
# parents = items.parents()
#
# print(type(parents))
# print(parents)



'''

兄弟元素
siblings


代码中doc('.list .item-0.active') 中的.tem-0和.active是紧挨着的，所以表示是并的关系，
这样满足条件的就剩下一个了：thired item的那个标签了

这样在通过.siblings就可以获取所有的兄弟标签，当然这里是不包括自己的
同样的在.siblings()里也是可以通过CSS选择器进行筛选

'''

html6 = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''

# doc = pq(html6)
# li = doc('.list .item-0.active')
# print(li.siblings())


'''

遍历
单个元素

'''

html7 = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
</div>
'''

# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
#
# lis = doc('li').items()
# print(type(lis))
#
# for li in lis:
#     print(type(li))
#     print(li)


'''

获取信息
获取属性
pyquery对象.attr(属性名)
pyquery对象.attr.属性名

'''

html8 = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''

# doc = pq(html)
# a = doc('.item-0.active a')
# print(a)
# print(a.attr('href'))
# print(a.attr.href)



'''

获取文本
在很多时候我们是需要获取被html标签包含的文本信息,通过.text()就可以获取文本信息

'''
html9 = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''

# doc = pq(html)
# a = doc('.item-0.active a')
# print(a)
# print(a.text())


'''

获取html
我们通过.html()的方式可以获取当前标签所包含的html信息

'''

html10 = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''

# doc = pq(html10)
# li = doc('.item-0.active')
# print(li)
# print(li.html())



'''

DOM操作
addClass、removeClass
熟悉前端操作的话，通过这两个操作可以添加和删除属性

'''

html11 = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''

# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
#
# li.removeClass('active')
# print(li)
#
# li.addClass('active')
# print(li)


'''

attr,css
同样的我们可以通过attr给标签添加和修改属性，
如果之前没有该属性则是添加，如果有则是修改
我们也可以通过css添加一些css属性，这个时候，标签的属性里会多一个style属性

'''

html12 = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''

# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
#
# li.attr('name', 'link')
# print(li)
#
# li.css('font-size', '14px')
# print(li)


'''

remove
有时候我们获取文本信息的时候可能并列的会有一些其他标签干扰，这个时候通过remove就可以将无用的或者干扰的标签直接删除
，从而方便操作

'''


html13 = '''
<div class="wrap">
    Hello, World
    <p>This is a paragraph.</p>
 </div>
'''

doc = pq(html13)
wrap = doc('.wrap')
print(wrap.text())
wrap.find('p').remove()
print(wrap.text())


