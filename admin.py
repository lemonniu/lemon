#coding:utf-8

#导入django admin的方法

from django.contrib import admin
from .models import test#models里面创建的类名字


class Blogadmin(admin.ModelAdmin):
    list_display = ["title"]

#models里面创建的类名字,只能统一注册
#admin.site.register(test,Blogadmin)
    
#用Unicode函数实现打开网址就能看到title的功能，当然用以上方法加edit settings.py也可以实现
#easy_install django-admin. 在settings.py里面加入django_admin的installed app

admin.site.register(test)



