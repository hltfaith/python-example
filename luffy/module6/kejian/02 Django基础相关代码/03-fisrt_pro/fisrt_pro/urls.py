"""fisrt_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include,register_converter

from app01.urlconvert import MonConvert


# 注册定义的url转换器
register_converter(MonConvert,"mm")

from app01 import views



urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('timer/', views.timer), # views.timer(request)
    #
    # path('login.html/',views.login,name="Log"),

    # 路由配置:     路径--------->视图函数

    #
    # re_path(r'articles/2003/$', views.special_case_2003), # special_case_2003(request)
    #
    # re_path(r'^articles/([0-9]{4})/$', views.year_archive), # year_archive(request,2009)
    #
    # #re_path(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive), # month_archive(request,2009,12)
    #
    # re_path(r'^articles/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/$', views.month_archive), # month_archive(request,y=2009,m=12)

    # 分发:
    # re_path(r"^app01/",include(("app01.urls","app01"))),
    # re_path(r"^app02/",include(("app02.urls","app02"))),
    # path("articles/<path:year>",views.path_year) , # path_year(request,2001)

    path("articles/<mm:month>",views.path_month)








]


# import re
#
#
# re.search("articles/2003/","yuan/alex/articles/2003/yuan/123")



# import re
#
#
# re.search("^articles/([0-9]{4})/$","/articles/2004/04/")


