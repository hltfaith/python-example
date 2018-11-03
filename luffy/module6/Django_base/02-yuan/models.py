
# 生成用户表
import pymysql

#连接数据库
conn = pymysql.connect(host='10.111.111.61', port=3306, user='root', passwd='123456', db='web_yuan') #db：库名

#创建游标
cur = conn.cursor()
sql = '''
create table userinfo(
    user varchar(20) not null,
    pwd varchar(20) not null)
'''

#执行sql语句
cur.execute(sql)

# 提交
conn.commit()
#关闭指针对象
cur.close()
#关闭连接对象
conn.close()

'''

web框架 yuan功能总结

main.py: 启动文件,封装了socket

1 urls.py: 路径与视图函数映射关系  ---- url控制器

2 views.py 视图函数,固定有一个形式参数:environ -----视图函数,

3 templates文件夹: html文件   -----模板

4 models: 在项目启动前,在数据库中创建表结构    ----- 与数据库相关


'''
