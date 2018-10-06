from django.db import models

# Create your models here.
from django.db import models
'''
Book  ----   Publish 一对多

'''

class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name=models.CharField( max_length=32)
    age=models.IntegerField()
    # 一对一
    authordetail=models.OneToOneField(to="AuthorDetail",to_field="nid",on_delete=models.CASCADE)
    def __str__(self):
        return self.name

# 作者详情表
class AuthorDetail(models.Model):

    nid = models.AutoField(primary_key=True)
    birthday=models.DateField()
    telephone=models.BigIntegerField()
    addr=models.CharField( max_length=64)

# 出版社表
class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name=models.CharField( max_length=32)
    city=models.CharField( max_length=32)
    email=models.EmailField()


    def __str__(self):
        return self.name


class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField( max_length=32)
    publishDate=models.DateField()
    price=models.DecimalField(max_digits=5,decimal_places=2)



    # 一对多关系
    publish=models.ForeignKey(to="Publish",to_field="nid",on_delete=models.CASCADE,)
    '''
        publish_id INT ,
        FOREIGN KEY (publish_id) REFERENCES publish(id)

    '''

    #多对多
    authors =models.ManyToManyField(to="Author")

    '''
    CREATE  TABLE book_authors(
       id INT PRIMARY KEY auto_increment ,
       book_id INT ,
       author_id INT ,
       FOREIGN KEY (book_id) REFERENCES book(id),
       FOREIGN KEY (author_id) REFERENCES author(id)
        )
    '''


# class Book2Author(models.Model):
#
#     nid = models.AutoField(primary_key=True)
#     book=models.ForeignKey(to="Book")
#     author=models.ForeignKey(to="Author")

    def __str__(self):
        return self.title


















class Emp(models.Model):

    name=models.CharField(max_length=32)
    age=models.IntegerField()
    salary=models.DecimalField(max_digits=8,decimal_places=2)
    dep=models.CharField(max_length=32)
    province=models.CharField(max_length=32)






