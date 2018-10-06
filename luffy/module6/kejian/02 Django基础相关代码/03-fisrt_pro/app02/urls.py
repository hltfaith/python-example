from django.contrib import admin
from django.urls import path,re_path


from app02 import views




urlpatterns = [

   re_path("index/",views.index,name="index")
]
