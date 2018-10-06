from django.shortcuts import render,HttpResponse,redirect

# Create your views here.


from .models import Publish,Author,Book



def add_book(request):

    if request.method=="POST":
        title=request.POST.get("title")
        price=request.POST.get("price")
        pub_date=request.POST.get("pub_date")
        publish_id=request.POST.get("publish_id")
        authors_id_list=request.POST.getlist("authors_id_list") # checkbox,select

        book_obj=Book.objects.create(title=title,price=price,publishDate=pub_date,publish_id=publish_id)
        print(authors_id_list) # ['2', '3']

        book_obj.authors.add(*authors_id_list)



        return HttpResponse("success")


    publish_list=Publish.objects.all()
    author_list=Author.objects.all()

    return render(request,"addbook.html",{"author_list":author_list,"publish_list":publish_list})




def books(request):

    book_list=Book.objects.all()
    return render(request,"books.html",{"book_list":book_list})


def change_book(request,edit_book_id):
    edit_book_obj=Book.objects.filter(pk=edit_book_id).first()

    if  request.method=="POST":
        title=request.POST.get("title")
        price=request.POST.get("price")
        pub_date=request.POST.get("pub_date")
        publish_id=request.POST.get("publish_id")
        authors_id_list=request.POST.getlist("authors_id_list") # checkbox,select

        Book.objects.filter(pk=edit_book_id).update(title=title,price=price,publishDate=pub_date,publish_id=publish_id)
        # edit_book_obj.authors.clear()
        # edit_book_obj.authors.add(*authors_id_list)

        edit_book_obj.authors.set(authors_id_list)

        return redirect("/books/")




    publish_list=Publish.objects.all()
    author_list=Author.objects.all()

    return render(request,"editbook.html",{"edit_book_obj":edit_book_obj,"publish_list":publish_list,"author_list":author_list})


def delete_book(request,delete_book_id):


    Book.objects.filter(pk=delete_book_id).delete()

    return redirect("/books/")

