from django.shortcuts import render,HttpResponse

# Create your views here.





from app01.myforms import *


def reg(request):

    if request.method=="POST":

        print(request.POST)

        #form=UserForm({"name":"yu","email":"123@qq.com","xxxx":"alex"})


        form=UserForm(request.POST) # form表单的name属性值应该与forms组件字段名称一致

        print(form.is_valid()) # 返回布尔值

        if form.is_valid():
            print(form.cleaned_data)  # {"name":"yuan","email":"123@qq.com"}
        else:
            print(form.cleaned_data)  # {"email":"123@qq.com"}
            # print(form.errors)        # {"name":[".........."]}
            # print(type(form.errors))  # ErrorDict
            # print(form.errors.get("name"))
            # print(type(form.errors.get("name")))    # ErrorList
            # print(form.errors.get("name")[0])


            #   全局钩子错误
            #print("error",form.errors.get("__all__")[0])
            errors=form.errors.get("__all__")


            return render(request,"reg.html",locals())

        '''

        form.is_valid()   :返回布尔值
        form.cleaned_data :{"name":"yuan","email":"123@qq.com"}
        form.errors       :{"name":[".........."]}

        '''


    form=UserForm()

    return render(request,"reg.html",locals())