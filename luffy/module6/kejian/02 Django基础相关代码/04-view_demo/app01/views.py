from django.shortcuts import render,HttpResponse,redirect

# Create your views here.


from django.shortcuts import HttpResponse

'''
http://127.0.0.1:8000/index/
url:协议://IP:port/路径?get请求数据

'''

def index(request):


    print("method",request.method)  #  "GET


    print(request.GET)
    print(request.GET.get("name"))
    print(request.POST)

    print(request.path)
    print(request.get_full_path())



    import time

    ctime=time.time()


    #return HttpResponse("<h1>OK</h1>")

    return render(request,"index.html",{"timer":ctime}) #  index.html 模板文件






def login(request):


    if request.method=="POST":

        user=request.POST.get("user")
        pwd=request.POST.get("pwd")

        if user=="alex" and pwd=="123":

            #return HttpResponse("success!")

            return redirect("/index/")


    return render(request,"login.html")


