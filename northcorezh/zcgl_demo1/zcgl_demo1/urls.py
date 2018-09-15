"""zcgl_demo1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path

from asset import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.asset),
    path('asset/', views.asset),
    path('export_excel/', views.export_excel),
    path('addasset/', views.addasset),
    re_path(r'asset/(\d+)/change', views.changeasset),
    re_path(r'asset/(\d+)/delete', views.delasset)
]
