from django.shortcuts import render,HttpResponse

# Create your views here.




def index(request):
    print("index.....")
    #yuan
    return HttpResponse("INDEX")



def index_new(request):


    return HttpResponse("index_new")