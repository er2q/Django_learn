"""day16 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve
from django.contrib import admin
from app01.views import depart, user, pretty_num, admin, account, task, order, chart, upload, kq_task

urlpatterns = [

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),

    # 部门管理
    path('depart/list/', depart.depart_list),
    path('depart/add/', depart.depart_add),
    path('depart/delete/', depart.depart_delete),
    # http://127.0.0.1:8000/depart/1/edit/
    path('depart/<int:nid>/edit/', depart.depart_edit),
    path('depart/multi/', depart.depart_multi),

    # 用户管理
    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/model/form/add/', user.user_model_form_add),
    # http://127.0.0.1:8000/depart/1/edit/
    path('user/<int:nid>/edit/', user.user_edit),
    path('user/<int:nid>/delete/', user.user_delete),

    # 靓号管理
    path('num/list/', pretty_num.num_list),
    path('num/model/form/add/', pretty_num.num_model_form_add),
    # http://127.0.0.1:8000/depart/1/edit/
    path('num/<int:nid>/edit/', pretty_num.num_edit),
    path('num/<int:nid>/delete/', pretty_num.num_delete),

    # 管理员管理
    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),
    # http://127.0.0.1:8000/depart/1/edit/
    path('admin/<int:nid>/edit/', admin.admin_edit),
    path('admin/<int:nid>/reset/', admin.admin_reset),
    path('admin/<int:nid>/delete/', admin.admin_delete),

    # 登录
    path('login/', account.login),
    path('logout/', account.logout),
    path('image/code/', account.image_code),

    # 任务管理
    path('task/', task.task_list),
    path('task/ajax/', task.task_ajax),
    path('task/add/', task.task_add),

    # 订单管理
    path('order/list/', order.order_list),
    path('order/add/', order.order_add),
    path('order/delete/', order.order_delete),
    path('order/ditail/', order.order_ditail),
    path('order/edit/', order.order_edit),

    # 数据统计
    path('chart/list/', chart.chart_list),
    path('chart/bar/', chart.chart_bar),

    # 上传文件
    path('upload/list/', upload.upload_list),
    path('upload/form/', upload.upload_form),
    path('upload/modal/form/', upload.upload_modal_form),

    # 城市列表
    path('city/list/', upload.city_list),

    # kq任务管理
    path('kq_task/list/', kq_task.task_list),
    path('kq_task/add/', kq_task.task_add),
    path('kq_task/delete/', kq_task.task_delete),
    path('kq_task/ditail/', kq_task.task_ditail),
    path('kq_task/edit/', kq_task.task_edit),
]
