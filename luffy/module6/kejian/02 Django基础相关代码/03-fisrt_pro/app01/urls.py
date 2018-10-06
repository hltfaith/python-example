from django.contrib import admin
from django.urls import path,re_path


from app01 import views



urlpatterns = [

    # re_path(r'articles/2003/$', views.special_case_2003,name="s_c_2003"), # special_case_2003(request)
    #
    # re_path(r'^articles/([0-9]{4})/$', views.year_archive,name="y_a"), # year_archive(request,2009)
    #
    # #re_path(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive), # month_archive(request,2009,12)
    #
    re_path(r'^articles/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/$', views.month_archive), # month_archive(request,y="2001",m="12")
    #
    # re_path("index/",views.index,name="index"),

]
