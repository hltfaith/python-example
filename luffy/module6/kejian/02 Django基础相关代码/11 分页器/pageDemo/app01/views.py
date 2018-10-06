from django.shortcuts import render

# Create your views here.


from .models import Book

from django.core.paginator import Paginator,EmptyPage

def index(request):
    '''
    批量导入:
    book_list=[]
    for i in range(100):
        book=Book(title="book_%s"%i,price=i*i)
        book_list.append(book)

    Book.objects.bulk_create(book_list)
    :param request:
    :return:
    '''


    book_list=Book.objects.all()

    # 分页器

    paginator=Paginator(book_list,3)

    print("count:",paginator.count)           #数据总数
    print("num_pages",paginator.num_pages)    #总页数
    print("page_range",paginator.page_range)  #页码的列表

    current_page_num=int(request.GET.get("page",1))

    if paginator.num_pages>11:

        if current_page_num-5<1:
            page_range=range(1,12)
        elif current_page_num+5>paginator.num_pages:
            page_range=range(paginator.num_pages-10,paginator.num_pages+1)

        else:
            page_range=range(current_page_num-5,current_page_num+6)
    else:
        page_range=paginator.page_range



    try:


        current_page=paginator.page(current_page_num)

        # 显示某一页具体数据的两种方式:
        print("object_list",current_page.object_list)
        for i in current_page:
            print(i)

    except EmptyPage as e:
         current_page=paginator.page(1)


    return render(request,"index.html",locals())