from django.shortcuts import render,HttpResponse

# Create your views here.


from django.urls import reverse

def timer(request):

    import time
    ctime=time.time()

    url=reverse("s_c_2003")
    url=reverse("y_a",args=(3333,)) # app01/articles/([0-9]{4})/


    print(url)


    return render(request,"timer.html",{"date":ctime})



from django.urls import reverse

def special_case_2003(request):


    return HttpResponse("special_case_2003")



def year_archive(request,year):


    return HttpResponse(year)



def month_archive(request,m,y):
    print(m)  #  12
    print(type(m))
    print(y)
    print(type(y))

    m=int(m)


    return HttpResponse(y+"-"+m)




def path_year(request,year):


    print(year)
    print(type(year))

    return HttpResponse("path year...")

def path_month(request,month):
    print(month,type(month))

    return HttpResponse("path month...")


def login(request):


    print(request.method)

    if request.method=="GET":
        return render(request,"login.html")

    else:
        print(request.GET)
        print(request.POST)
        user=request.POST.get("user")
        pwd=request.POST.get("pwd")

        if user=="yuan" and pwd=="123":
            return HttpResponse("登录成功!")
        else:
            return HttpResponse("用户名或者密码错误!")




from django.urls import reverse

def index(request):

    return HttpResponse(reverse("app01:index"))











