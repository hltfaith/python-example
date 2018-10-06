from django.shortcuts import render,HttpResponse

# Create your views here.




def index(request):
    '''
    模板语法:

    变量: {{}}
         1 深度查询   句点符
         2 过滤器  {{val|filter_name:参数}}

    标签: {% %}



    :param request:
    :return:
    '''
    ######################深度查询   句点符
    name="yuan"
    i=1
    l=[111,222,333]
    info={"name":"yuan","age":22}

    b=True

    class Person(object):

        def __init__(self,name,age):
            self.name=name
            self.age=age

    alex=Person("alex",35)
    egon=Person("egon",33)

    person_list=[alex,egon]


    #person_list=[]


    ######################过滤器

    import datetime
    now=datetime.datetime.now()
    file_size=12343242123123

    content="hello yuan xiao bisheng hello yuan xiao bisheng hello yuan xiao bisheng hello yuan xiao bisheng"


    link="<a href=''>click</a>"

    ###################### 标签


    user="alex"


    #return render(request,"index.html",{"n":name})
    return render(request,"index.html",locals())



def login(request):

    if request.method=="POST":

        return HttpResponse("OK")


    return render(request,"login.html")




def orders(request):

    return render(request,"orders.html")