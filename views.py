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

#��ΪURL��������Բ���ţ������м���Բ���ţ����������Ӧ�ö༸��,������ʽԲ���ſ���ȡֵ

def test(request,w):
    
    a = 5
    b = [1,2,3,4,5,6,7,8,9]
    
    #t = Template("My name is {{name}}.")
    #c = Context({'name':w})
    
    #return HttpResponse("Hello Test %s" % os.listdir('./lemon'))
    #return HttpResponse(t.render(c))
    
    return render_to_response("test.html",{'name':w,'a':a,'b':b})

#���ݿ����ɾ�Ĳ飨CRUD��
#ͬshell command��һ��

from lemon.models import test

def lemon_create(request):
    b = test()
    #��ȡ�û����������ݡ�
    #print request.POST#�����ʮ���ֵ� �����û��������http request��֤��Ϣ
    b.title = request.POST["title"]
    b.save()
    #д���ۣ���Ӧcreate.html ���textarea
    b.content = request.POST["content"]
    b.save()
    return redirect("/list")
    
def lemon_list(request):
    all = test.objects.filter().order_by("-id")
    #for ѭ����ģ������д
    #�ȷ���list.html Ȼ��������all �����ﺯ����all�滻
    return render_to_response("list1.html",{'all':all})
        
def lemon_update(request,id):
    b = test.objects.get(id=int(id))
    #��ȡ����b��ֵ�ش���ģ����ҳ
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


