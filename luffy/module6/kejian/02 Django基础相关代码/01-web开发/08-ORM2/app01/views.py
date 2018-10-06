from django.shortcuts import render, HttpResponse

# Create your views here.

from app01.models import *


def add(request):
    """
    绑定关系
    :param request:
    :return:
    """

    pub = Publish.objects.create(name="人民出版社", email="123@qq.com", city="北京")

    '''
    ######################绑定一对多的关系##############################################
    #方式1:
    #为book表绑定出版社: book  ---    publish
    book_obj=Book.objects.create(title="红楼梦",price=100,publishDate="2012-12-12",publish_id=1)
    print(book_obj.title)

    #方式2:

    pub_obj=Publish.objects.filter(nid=1).first()
    book_obj=Book.objects.create(title="三国演绎",price=100,publishDate="2012-12-12",publish=pub_obj)
    print(book_obj.title)
    print(book_obj.price)
    print(book_obj.publishDate)
    print(book_obj.publish)       #  与这本书籍关联的出版社对象
    print(book_obj.publish.name)
    print(book_obj.publish.email)
    print(book_obj.publish_id)

    #查询西游记的出版社对应的邮箱

    book_obj=Book.objects.filter(title="西游记").first()
    print(book_obj.publish.email)






    ######################绑定多对多的关系##############################################

    book_obj=Book.objects.create(title="金瓶梅",price=100,publishDate="2012-12-12",publish_id=1)

    egon=Author.objects.get(name="egon")
    alex=Author.objects.get(name="alex")

    #绑定多对多关系的API
    book_obj.authors.add(egon,alex)
    book_obj.authors.add(1,2,3)
    book_obj.authors.add(*[1,2,3])

    #解除多对多关系

    book=Book.objects.filter(nid=4).first()
    book.authors.remove(2)
    #book.authors.remove(*[1,2])

    book.authors.clear()


    #查询主键为4的书籍的所有作者的名字
    book=Book.objects.filter(nid=4).first()
    print(book.authors.all()) # [obj1,obj2...] queryset: 与这本书关联的所有作者对象集合
    ret=book.authors.all().values("name")
    print(ret)


    关键点:

    一 book_obj.publish=Publish.objects.filter(id=book_obj.publish_id).first()

    二 book_obj.authors.all()
       关键点:book.authors.all()  # 与这本书关联的作者集合

        1 book.id=3
        2 book_authors
            id  book_id  author_ID
            3	  3	         1
            4	  3	         2

        3  author
           id   name
           1   alex
           2   egon

    book_obj.authors.all()    ------->   [alex,egon]



    '''

    return HttpResponse("OK")


def query(request):
    """
    跨表查询:
       1 基于对象查询
       2 基于双下划线查询
       3 聚合和分组查询
       4 F 与 Q查询
    :param request:
    :return:
    """

    # -------------------------基于对象的跨表查询(子查询)-----------------------

    # 一对多查询的正向查询 : 查询金瓶梅这本书的出版社的名字

    # book_obj=Book.objects.filter(title="金瓶梅").first()
    # print(book_obj.publish) # 与这本书关联出版社对象
    # print(book_obj.publish.name)
    # 对应sql:
    # select publish_id from Book where title="金瓶梅"
    # select name from Publish where id=1


    # 一对多查询的反向查询 : 查询人民出版社出版过的书籍名称

    # publish=Publish.objects.filter(name="人民出版社").first()
    # ret=publish.book_set.all()
    # print(ret)

    # 多对多查询的正向查询 : 查询金瓶梅这本书的所有作者的名字

    # book_obj=Book.objects.filter(title="金瓶梅").first()
    # author_list=book_obj.authors.all() # queryset对象  [author_obj1,...]
    #
    # for author in author_list:
    #     print(author.name)

    # 多对多查询的反向查询 : 查询alex出版过的所有书籍名称

    # alex=Author.objects.filter(name="alex").first()
    #
    # book_list=alex.book_set.all()
    # for book in book_list:
    #     print(book.title)


    # 一对一查询的正向查询 : 查询alex的手机号

    # alex=Author.objects.filter(name="alex").first()
    # print(alex.authordetail.telephone)
    # # 一对一查询的反向查询 : 查询手机号为110的作者的名字和年龄
    #
    # ad=AuthorDetail.objects.filter(telephone="110").first()
    # print(ad.author.name)
    # print(ad.author.age)


    # -------------------------基于双下划线的跨表查询(join查询)-----------------------

    '''

    正向查询按字段,反向查询按表名小写用来告诉ORM引擎join哪张表

    '''

    # 一对多查询 : 查询金瓶梅这本书的出版社的名字

    # 方式1:
    # ret=Book.objects.filter(title="金瓶梅").values("publish__name")
    # print(ret) # <QuerySet [{'publish__name': '南京出版社'}]>

    # 方式2:
    # ret=Publish.objects.filter(book__title="金瓶梅").values("name")
    # print(ret)

    # 多对多查询 : 查询金瓶梅这本书的所有作者的名字

    # 方式1:

    # 需求: 通过Book表join与其关联的Author表,属于正向查询:按字段authors通知ORM引擎join book_authors与author

    # ret=Book.objects.filter(title="金瓶梅").values("authors__name")
    # print(ret) # <QuerySet [{'authors__name': 'alex'}, {'authors__name': 'egon'}]>


    # 方式2:
    # 需求: 通过Author表join与其关联的Book表,属于反向查询:按表名小写book通知ORM引擎join book_authors与book表
    # ret=Author.objects.filter(book__title="金瓶梅").values("name")
    # print(ret) # <QuerySet [{'name': 'alex'}, {'name': 'egon'}]>


    # 一对一查询的查询 : 查询alex的手机号

    # 方式1:
    # 需求: 通过Author表join与其关联的AuthorDetail表,属于正向查询:按字段authordetail通知ORM引擎join Authordetail表

    # ret=Author.objects.filter(name="alex").values("authordetail__telephone")
    # print(ret) # <QuerySet [{'authordetail__telephone': 110}]>
    #
    # # 方式2:
    # # 需求: 通过AuthorDetail表join与其关联的Author表,属于反向查询:按表名小写author通知ORM引擎join Author表
    # ret=AuthorDetail.objects.filter(author__name="alex").values("telephone")
    # print(ret) # <QuerySet [{'telephone': 110}]>

    # 进阶练习:

    # 练习: 手机号以110开头的作者出版过的所有书籍名称以及书籍出版社名称

    # 方式1:
    # 需求: 通过Book表join AuthorDetail表, Book与AuthorDetail无关联,所以必需连续跨表
    # ret=Book.objects.filter(authors__authordetail__telephone__startswith="110").values("title","publish__name")
    # print(ret)
    #
    # # 方式2:
    # ret=Author.objects.filter(authordetail__telephone__startswith="110").values("book__title","book__publish__name")
    # print(ret)


    # -------------------------聚合与分组查询---------------------------


    # ------------------------->聚合 aggregate:返回值是一个字典,不再是queryset

    # 查询所有书籍的平均价格
    from django.db.models import Avg, Max, Min, Count

    ret = Book.objects.all().aggregate(avg_price=Avg("price"), max_price=Max("price"))
    print(ret)  # {'avg_price': 151.0, 'max_price': Decimal('301.00')}

    # ------------------------->分组查询 annotate ,返回值依然是queryset


    # ------------------------->单表分组查询:

    # 示例1
    # 查询每一个部门的名称以及员工的平均薪水

    # select dep,Avg(salary) from emp group by dep

    # ret=Emp.objects.values("dep").annotate(avg_salary=Avg("salary"))
    # print(ret) # <QuerySet [{'avg_salary': 5000.0, 'dep': '保安部'}, {'avg_salary': 51000.0, 'dep': '教学部'}]>

    # 单表分组查询的ORM语法: 单表模型.objects.values("group by的字段").annotate(聚合函数("统计字段"))

    # 示例2
    # 查询每一个省份的名称以及员工数

    # ret=Emp.objects.values("province").annotate(c=Count("id"))
    #
    # print(ret) # <QuerySet [{'province': '山东省', 'c': 2}, {'province': '河北省', 'c': 1}]>

    # 补充知识点:

    # ret=Emp.objects.all()
    # print(ret)  # select * from emp
    # ret=Emp.objects.values("name")
    # print(ret)  # select name from emp
    #
    # Emp.objects.all().annotate(avg_salary=Avg("salary"))


    # ------------------------->多表分组查询:

    ## 示例1 查询每一个出版社的名称以及出版的书籍个数

    ret = Publish.objects.values("nid").annotate(c=Count("book__title"))
    print(ret)  # <QuerySet [{'nid': 1, 'c': 3}, {'nid': 2, 'c': 1}]>

    ret = Publish.objects.values("name").annotate(c=Count("book__title"))
    print(ret)  # <QuerySet [{'name': '人民出版社', 'c': 3}, {'name': '南京出版社', 'c': 1}]>

    ret = Publish.objects.values("nid").annotate(c=Count("book__title")).values("name", "c")
    print(ret)  # <QuerySet [{'name': '人民出版社', 'c': 3}, {'name': '南京出版社', 'c': 1}]>

    ## 示例2 查询每一个作者的名字以及出版过的书籍的最高价格
    ret = Author.objects.values("pk").annotate(max_price=Max("book__price")).values("name", "max_price")
    print(ret)

    # 总结 跨表的分组查询的模型:
    # 每一个后表模型.objects.values("pk").annotate(聚合函数(关联表__统计字段))

    # 示例3 查询每一个书籍的名称以及对应的作者个数
    ret = Book.objects.values("pk").annotate(c=Count("authors__name")).values("title", "c")
    print(ret)

    #################### 跨表分组查询的另一种玩法  ####################

    # 示例1 查询每一个出版社的名称以及出版的书籍个数
    # ret=Publish.objects.values("nid").annotate(c=Count("book__title")).values("name","email","c")
    # ret=Publish.objects.all().annotate(c=Count("book__title")).values("name","c","city")
    ret=Publish.objects.annotate(c=Count("book__title")).values("name","c","city")
    print(ret)

    ##################### 练习   ####################

    # 统计每一本以py开头的书籍的作者个数：

    # 每一个后的表模型.objects.values("pk").annotate(聚合函数(关联表__统计字段)).values("表模型的所有字段以及统计字段")
    ret=Book.objects.filter(title__startswith="py").values("pk").annotate(c=Count("authors__name")).values("title","c")

    # 统计不止一个作者的图书
    ret=Book.objects.values("pk").annotate(c=Count("authors__name")).filter(c__gt=1).values("title","c")
    print(ret)


    















































































    return HttpResponse("查询成功")
