# -*- coding:UTF-8 -*-

# datetime:2022/6/15 14:49
# software: PyCharm
"""
//
//                       .::::.
//                     .::::::::.
//                    :::::::::::
//                 ..:::::::::::'
//              '::::::::::::'
//                .::::::::::
//           '::::::::::::::..
//                ..::::::::::::.
//              ``::::::::::::::::
//               ::::``:::::::::'        .:::.
//              ::::'   ':::::'       .::::::::.
//            .::::'      ::::     .:::::::'::::.
//           .:::'       :::::  .:::::::::' ':::::.
//          .::'        :::::.:::::::::'      ':::::.
//         .::'         ::::::::::::::'         ``::::.
//     ...:::           ::::::::::::'              ``::.
//    ```` ':.          ':::::::::'                  ::::..
//                       '.:::::'                    ':'````..
"""
"""
文件说明：
    
"""
# -*- coding:UTF-8 -*-

# datetime:2022/6/15 13:12
# software: PyCharm
"""
//
//                       .::::.
//                     .::::::::.
//                    :::::::::::
//                 ..:::::::::::'
//              '::::::::::::'
//                .::::::::::
//           '::::::::::::::..
//                ..::::::::::::.
//              ``::::::::::::::::
//               ::::``:::::::::'        .:::.
//              ::::'   ':::::'       .::::::::.
//            .::::'      ::::     .:::::::'::::.
//           .:::'       :::::  .:::::::::' ':::::.
//          .::'        :::::.:::::::::'      ':::::.
//         .::'         ::::::::::::::'         ``::::.
//     ...:::           ::::::::::::'              ``::.
//    ```` ':.          ':::::::::'                  ::::..
//                       '.:::::'                    ':'````..
"""
"""
文件说明：

"""
import random

from django.shortcuts import render, redirect

from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.form import AdminModelForm, AdminEditModelForm, AdminResetModelForm


# ################################# 管理员管理 ##########################
def admin_list(request):
    """ 管理员列表 """
    # for i in range(20):
    #     password = str(int(random.uniform(13, 20)*10e8))
    #     models.Admin.objects.create(username=f"张三{i}", password=password)

    # 检查用户是否已经登录，已经登录，继续向下走，未登录，跳转回登录页面。
    # 用户发来请求，获取cookie随机字符串，拿着随机字符串看看session中有没有
    # request.session["info"]
    # info = request.session.get("info", "")
    # if not info:
    #     return redirect("/login/")

    queryset = models.Admin.objects.all()
    page_object = Pagination(request, queryset=queryset)

    context = {
        'queryset': page_object.page_queryset,  # 分完页数据
        "page_string": page_object.html()  # 页码
    }
    return render(request, 'admin_list.html', context)


def admin_add(request):
    """ 添加管理员 ModelForm版本 """
    title = "新建管理员"
    if request.method == "GET":
        form = AdminModelForm()
        return render(request, "change.html", {"form": form, "title": title})

    # 用户POST提交数据，数据校验
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        return redirect("/admin/list/")
    # 校验失败 （在页面上显示错误信息）
    return render(request, "change.html", {"form": form, "title": title})


def admin_delete(request, nid):
    """ 删除管理员 """
    # 删除
    models.Admin.objects.filter(id=nid).delete()
    # 跳转回部门列表
    return redirect('/admin/list')


def admin_edit(request, nid):
    """ 编辑管理员 """
    # 根据nid，获取它的数据 【obj】
    row_object = models.Admin.objects.filter(id=nid).first()
    # 空
    if not row_object:
        return redirect("/admin/list/")

    title = "重置密码"
    if request.method == "GET":
        form = AdminEditModelForm(instance=row_object)
        return render(request, 'change.html', {"form": form, "title": title})

    # 用户POST提交数据，数据校验
    form = AdminEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        return redirect("/admin/list/")
    # 校验失败 （在页面上显示错误信息）
    return render(request, "change.html", {"form": form, "title": title})


def admin_reset(request, nid):
    """ 重置密码 """
    # 根据nid，获取它的数据 【obj】
    row_object = models.Admin.objects.filter(id=nid).first()
    # 空
    if not row_object:
        return redirect("/admin/list/")

    title = "重置密码"
    if request.method == "GET":
        form = AdminResetModelForm()
        return render(request, 'change.html', {"form": form, "title": title})

    # 用户POST提交数据，数据校验
    form = AdminResetModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        return redirect("/admin/list/")
    # 校验失败 （在页面上显示错误信息）
    return render(request, "change.html", {"form": form, "title": title})
