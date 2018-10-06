from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

from app01.models import Book

def addbook(request):
    if request.method=="POST":

        title=request.POST.get("title")
        price=request.POST.get("price")
        date=request.POST.get("date")
        publish=request.POST.get("publish")


        book_obj=Book.objects.create(title=title,price=price,pub_date=date,publish=publish)

        return redirect("/books/")

    return render(request,"addbook.html")



def books(request):


    book_list=Book.objects.all() # [obj1,obj2,....]


    return render(request,"books.html",locals())





def changebook(request,id):
    book_obj=Book.objects.filter(id=id).first()

    if request.method=="POST":
        title=request.POST.get("title")
        price=request.POST.get("price")
        date=request.POST.get("date")
        publish=request.POST.get("publish")

        Book.objects.filter(id=id).update(title=title,price=price,pub_date=date,publish=publish)

        return redirect("/books/")

    return render(request,"changebook.html",{"book_obj":book_obj})







def delbook(request,id):

    Book.objects.filter(id=id).delete()

    return redirect("/books/")





def query(request):


    # 查询老男孩出版社出版过的价格大于200的书籍
    ret=Book.objects.filter(publish="老男孩出版社",price__gt=200)

    # 查询2017年8月出版的所有以py开头的书籍名称
    ret=Book.objects.filter(title__startswith="py",pub_date__year=2017,pub_date__month=8).values("title")

    #查询价格为50,100或者150的所有书籍名称及其出版社名称

    ret=Book.objects.filter(price__in=[50,100,150]).values("title","publish")


    #  查询价格在100到200之间的所有书籍名称及其价格

    ret=Book.objects.filter(price__range=[100,200]).values("title","publish")

    #  查询所有人民出版社出版的书籍的价格（从高到低排序，去重）

    ret=Book.objects.filter(publish="人民出版社").values("price").distinct().order_by("-price")



    return HttpResponse("OK")
