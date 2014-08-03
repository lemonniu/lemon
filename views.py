# -*- coding: cp936 -*-
#coding:utf-8

from django.http import HttpResponse
import datetime
import os
from django.template import Template,Context
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext

def home(request):
    
    return HttpResponse("Hello World")

#因为URL定义用了圆括号，所以有几个圆括号，输入参数就应该多几个,正则表达式圆括号可以取值

def test(request,w):
    
    a = 5
    b = [1,2,3,4,5,6,7,8,9]
    
    #t = Template("My name is {{name}}.")
    #c = Context({'name':w})
    
    #return HttpResponse("Hello Test %s" % os.listdir('./lemon'))
    #return HttpResponse(t.render(c))
    
    return render_to_response("test.html",{'name':w,'a':a,'b':b})

#数据库的增删改查（CRUD）
#同shell command中一样

from lemon.models import test

def lemon_create(request):
    b = test()
    #获取用户的输入内容。
    #print request.POST#输出的十个字典 包括用户的输入和http request验证信息
    b.title = request.POST["title"]
    b.save()
    #写评论，对应create.html 里的textarea
    b.content = request.POST["content"]
    b.save()
    return redirect("/list")
    
def lemon_list(request):
    all = test.objects.filter().order_by("-id")
    #for 循环在模板里面写
    #先访问list.html 然后把里面的all 用这里函数的all替换
    return render_to_response("list1.html",{'all':all})
        
def lemon_update(request,id):
    b = test.objects.get(id=int(id))
    #把取到的b的值回传到模板网页
    return render_to_response("update.html",{'b':b},context_instance=RequestContext(request))
    #b.title = "update blog test"
    #b.save()
    #return redirect("/list")

def lemon_delete(request,id):
    b = test.objects.get(id=int(id))
    b.delete()
    return redirect("/list")
    

def test1(request):
    
    return HttpResponse("Hello Test1 %s" % datetime.datetime.now())

def lemon_create_form(request):
    
    return render_to_response("create.html",context_instance=RequestContext(request))

def update_blog(request,id):
    b = test.objects.get(id=int(id))
    b.title = request.POST["title"]
    #b.save()
    b.content = request.POST["content"]
    b.save()
    return redirect("/list")


