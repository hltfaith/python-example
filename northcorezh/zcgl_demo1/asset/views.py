from django.shortcuts import render, redirect

# Create your views here.

from asset.models import asset_db
from asset.tests import xslx_data
#import export_xslx

def asset(request):

    db_data = asset_db.objects.all()

    return render(request, 'asset.html', locals())


def export_excel(request):


    # 将转换好的excel数据,写入到数据库
    data = xslx_data()

    # 字典遍历出来,写入数据库
    for i in data:
        val = data[i].strip('[]')
        val = str(val).split(",")

        asset_db.objects.create(hostname=eval(val[0]), ip_addr=eval(val[1]), username=eval(val[2]),
                                password=eval(val[3]),
                                model=eval(val[4]), sn=eval(val[5]), local=eval(val[6]), resource_type=eval(val[7]),
                                port=eval(val[8]),
                                system_version=eval(val[9]), group=eval(val[10])
                                )

    return redirect("/asset/")


def addasset(request):

    if request.method == "POST":
        hostname = request.POST.get("hostname")
        ip_addr = request.POST.get("ip_addr")
        username = request.POST.get("username")
        password = request.POST.get("password")

        model = request.POST.get("model")
        sn = request.POST.get("sn")
        local = request.POST.get("local")
        resource_type = request.POST.get("resource_type")

        port = request.POST.get("port")
        system_version = request.POST.get("system_version")
        group = request.POST.get("group")

        asset_obj = asset_db.objects.create(
            hostname=hostname, ip_addr=ip_addr, username=username, password=password,
            model=model, sn=sn, local=local, resource_type=resource_type, port=port,
            system_version=system_version, group=group
        )

        return redirect("/asset/")

    return render(request, "addasset.html")


def changeasset(request, id):
    asset_obj = asset_db.objects.filter(id=id).first()

    if request.method == "POST":
        hostname = request.POST.get("hostname")
        ip_addr = request.POST.get("ip_addr")
        username = request.POST.get("username")
        password = request.POST.get("password")

        model = request.POST.get("model")
        sn = request.POST.get("sn")
        local = request.POST.get("local")
        resource_type = request.POST.get("resource_type")

        port = request.POST.get("port")
        system_version = request.POST.get("system_version")
        group = request.POST.get("group")

        asset_db.objects.filter(id=id).update(
            hostname=hostname, ip_addr=ip_addr, username=username, password=password,
            model=model, sn=sn, local=local, resource_type=resource_type, port=port,
            system_version=system_version, group=group
        )

        return redirect("/asset/")

    return render(request, "changeasset.html", {"asset_obj": asset_obj})


def delasset(request,id):
    asset_db.objects.filter(id=id).delete()

    return redirect("/asset/")












































