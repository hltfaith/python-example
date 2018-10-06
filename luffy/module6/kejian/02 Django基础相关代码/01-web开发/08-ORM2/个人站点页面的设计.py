个人站点页面设计（ORM跨表与分组查询）



查询：



日期归档查询



   1    date_format

        ============date,time,datetime===========

		create table t_mul_new(d date,t time,dt datetime);

		insert into t_mul_new values(now(),now(),now());

		select * from t_mul;


		mysql> select * from t_mul;
		+------------+----------+---------------------+
		| d          | t        | dt                  |
		+------------+----------+---------------------+
		| 2017-08-01 | 19:42:22 | 2017-08-01 19:42:22 |
		+------------+----------+---------------------+
		1 row in set (0.00 sec)


		select date_format(dt,"%Y/%m/%d") from t_mul;




   2  extra
        

        extra(select=None, where=None, params=None, tables=None, order_by=None, select_params=None)

		有些情况下，Django的查询语法难以简单的表达复杂的 WHERE 子句，对于这种情况, Django 提供了 extra() QuerySet修改机制 — 它能在 QuerySet生成的SQL从句中注入新子句

		extra可以指定一个或多个 参数,例如 select, where or tables. 这些参数都不是必须的，但是你至少要使用一个!要注意这些额外的方式对不同的数据库引擎可能存在移植性问题.(因为你在显式的书写SQL语句),除非万不得已,尽量避免这样做

		参数之select

		The select 参数可以让你在 SELECT 从句中添加其他字段信息，它应该是一个字典，存放着属性名到 SQL 从句的映射。

		queryResult=models.Article
		　　　　　　　　　　　.objects.extra(select={'is_recent': "create_time > '2017-09-05'"})
		结果集中每个 Entry 对象都有一个额外的属性is_recent, 它是一个布尔值，表示 Article对象的create_time 是否晚于2017-09-05.

		练习：

		in sqlite:

		    article_obj=models.Article.objects
		　　　　　　　　　　　　　　.extra(select={"standard_time":"strftime('%%Y-%%m-%%d',create_time)"})
		　　　　　　　　　　　　　　.values("standard_time","nid","title")
		    print(article_obj)
		    # <QuerySet [{'title': 'MongoDb 入门教程', 'standard_time': '2017-09-03', 'nid': 1}]>



   3  单表分组查询

      ......































