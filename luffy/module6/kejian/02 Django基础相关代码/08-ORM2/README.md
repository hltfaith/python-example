A-B
关联属性在A表中

正向查询: A------>B
反向查询: B------>A

基于对象的跨表查询(子查询)

    # 一对多查询
           正向查询:按字段
           反向查询:表名小写_set.all()


                                     book_obj.publish
            Book(关联属性:publish)对象  --------------> Publish对象
                                     <--------------
                                 publish_obj.book_set.all()  # queryset



    # 多对多查询
           正向查询:按字段
           反向查询:表名小写_set.all()

                                     book_obj.authors.all()
            Book(关联属性:authors)对象  ------------------------> Author对象
                                     <------------------------
                                     author_obj.book_set.all() # queryset



    # 一对一查询

           正向查询:按字段
           反向查询:表名小写

                                              author.authordetail
            Author(关联属性:authordetail)对象  ------------------------>AuthorDetail对象
                                             <------------------------
                                              authordetail.author

基于双下划线的跨表查询(join查询)

     key:正向查询按字段,反向查询按表名小写


单表的分组查询:


    查询每一个部门名称以及对应的员工数

    emp:

    id  name age   salary    dep
    1   alex  12   2000     销售部
    2   egon  22   3000     人事部
    3   wen   22   5000     人事部


    sql :  select Count(id) from emp group by dep;

    思考:如何用ORM语法进行分组查询?


    # 单表分组查询的ORM语法: 单表模型.objects.values("group by的字段").annotate(聚合函数("统计字段"))

    在单表分组下,按着主键进行group by是没有任何意义的.


跨表的分组查询:

     Book表

        id   title    date      price  publish_id
        1	红楼梦	2012-12-12	101	   1
        2	西游记	2012-12-12	101	   1
        3	三国演绎	2012-12-12	101	   1
        4	金瓶梅	2012-12-12	301	   2


     Publish表
        id    name      addr   email
        1	人民出版社	北京	   123@qq.com
        2	南京出版社	南京	   345@163.com


     1 查询每一个出版社出版的书籍个数
     Book.objects.values("publish_id").annotate(Count("id"))

     2 示例1 查询每一个出版社的名称以及出版的书籍个数
         join sql : select * from Book inner join Publish on book.publish_id=publish.id

        id   title    date      price  publish_id   publish.id  publish.name  publish.addr  publish.email
        1	红楼梦	2012-12-12	101	   1            1	           人民出版社	       北京	     123@qq.com
        2	西游记	2012-12-12	101	   1            1	           人民出版社	       北京	     123@qq.com
        3	三国演绎	2012-12-12	101	   1            1	           人民出版社	       北京	     123@qq.com
        4	金瓶梅	2012-12-12	301	   2            2	           南京出版社	       南京	     345@163.com


        分组查询sql:
           select publish.name,Count("title") from Book inner join Publish on book.publish_id=publish.id
               group by  publish.id,publish.name,publish.addr,publish.email

        思考:如何用ORM语法进行跨表分组查询

         ret=Publish.objects.values("nid").annotate(c=Count("book__title")).values("name","c")
         print(ret)

     3 示例2 查询每一个作者的名字以及出版过的书籍的最高价格
        ret=Author.objects.values("pk").annotate(max_price=Max("book__price")).values("name","max_price")

     4 示例3 查询每一个书籍的名称以及对应的作者个数

       ret=Book.objects.values("pk").annotate(c=Count("authors__name")).values("title","c")
       print(ret)

     5 总结:
          # 总结 跨表的分组查询的模型:
          # 每一个后的表模型.objects.values("pk").annotate(聚合函数(关联表__统计字段)).values("表模型的所有字段以及统计字段")
          # 每一个后的表模型.objects.annotate(聚合函数(关联表__统计字段)).values("表模型的所有字段以及统计字段")















































