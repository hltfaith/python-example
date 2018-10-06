from django.shortcuts import render,HttpResponse

# Create your views here.


from app01.models import Book

def index(request):


    # ==================================添加表记录 ==================================

    # 方式1:
    # book_obj=Book(id=1,title="python红宝书",price=100,pub_date="2012-12-12",publish="人民出版社")
    # book_obj.save()

    #方式2: create返回值就是当前生成的对象纪录

    #book_obj=Book.objects.create(title="php2",price=100,pub_date="2013-12-12",publish="人民出版社")
    #print(book_obj.title)
    # print(book_obj.price)
    # print(book_obj.pub_date)

    # ================================== 查询表记录API ==================================
    '''
      1 方法的返回值
      2 方法的调用这

    '''
    #(1) all方法:   返回值一个queryset对象

    #book_list=Book.objects.all()
    #print(book_list)  # [obj1,obj2,.....]

    # for  obj in book_list:
    #     print(obj.title,obj.price)

    #print(book_list[1].title)

    #(2) first,last : 调用者:queryset对象  返回值:model对象

    #book=Book.objects.all().first()
    #book=Book.objects.all()[0]


    #(3) filter()  返回值:queryset对象

    # book_list=Book.objects.filter(price=100)     # [obj1,obj2,....]
    # print(book_list) #<QuerySet [<Book: python红宝书>, <Book: php>]>
    # book_obj=Book.objects.filter(price=100).first()

    # ret=Book.objects.filter(title="go",price=200)
    # print(ret)

    #(4) get()  有且只有一个查询结果时才有意义  返回值:model对象


    # book_obj=Book.objects.get(title="go")
    # book_obj=Book.objects.get(price=100)
    # print(book_obj.price)

    # (5) exclude 返回值:queryset对象
    # ret=Book.objects.exclude(title="go")
    # print(ret)

    # (6) order_by   调用者: queryset对象   返回值:  queryset对象
    # ret=Book.objects.all().order_by("-id")
    # ret=Book.objects.all().order_by("price","id")
    # print(ret)


    # (7) count()   调用者: queryset对象   返回值: int
    # ret=Book.objects.all().count()
    # print(ret)


    # (8) exist()

    # ret=Book.objects.all().exists()
    #
    # if ret:
    #     print("ok")



    # (9) values 方法  调用者: queryset对象  返回值:queryset对象

    # ret=Book.objects.all()
    # for i in ret:
    #     print(i.title)

    # ret=Book.objects.all().values("price","title")

    '''
    values:

    temp=[]

    for obj in Book.objects.all()
         temp.append({
             "price"=obj.price
             "title"=obj.title
         })

    return temp

    '''
    #print(ret)

    # <QuerySet [{'price': Decimal('100.00')}, {'price': Decimal('100.00')}, {'price': Decimal('200.00')}]>
    #print(ret[0].get("price")) # 100.00


    # (10) values_list 方法  调用者: queryset对象  返回值:queryset对象

    # ret=Book.objects.all().values_list("price","title")
    # # print(ret) #<QuerySet [(Decimal('100.00'),), (Decimal('100.00'),), (Decimal('200.00'),)]>
    # print(ret)

    '''
values:
    <QuerySet [{'title': 'python红宝书', 'price': Decimal('100.00')}, {'title': 'php', 'price': Decimal('100.00')}, {'title': 'go', 'price': Decimal('200.00')}]>
values_list:
    <QuerySet [(Decimal('100.00'), 'python红宝书'), (Decimal('100.00'), 'php'), (Decimal('200.00'), 'go')]>

    '''

    # 11 distinct

    # ret=Book.objects.all().distinct()
    # print(ret)

    # ret=Book.objects.all().values("price").distinct()
    # print(ret)

    #Book.objects.all().filter().order_by().filter().reverse().first()




    # ================================== 查询表记录之模糊查询 ==================================

    # ret=Book.objects.filter(price__gt=10,price__lt=200)
    # print(ret)
    #
    # ret=Book.objects.filter(title__startswith="p")

    #ret=Book.objects.filter(title__contains="h")
    #ret=Book.objects.filter(title__icontains="h")


    #ret=Book.objects.filter(price__in=[200,300])

    #ret=Book.objects.filter(pub_date__year=2018,pub_date__month=5)
    #print(ret)



    # ================================== 删除纪录和修改纪录 ===============================

    # delete: 调用者: queryset对象  model对象

    # ret=Book.objects.filter(price=100).delete()
    # print(ret)

    # Book.objects.filter(price=100).first().delete()



    # update :  调用者: queryset对象
    ret=Book.objects.filter(title="php2").update(title="php")





















    return HttpResponse("OK")
