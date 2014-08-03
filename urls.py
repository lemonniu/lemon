# -*- coding: cp936 -*-
#using:utf-8

from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lemon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^lemon_create_form$', 'lemon.views.lemon_create_form'),
    url(r'^update_blog/(\d+)$', 'lemon.views.update_blog'),
    url(r'^home$', 'lemon.views.home'),
    url(r'^test/(\w+)$', 'lemon.views.test'),
    url(r'^test1/\w+$', 'lemon.views.test1'),
    url(r'^blog_create$', 'lemon.views.lemon_create'),
    url(r'^list$', 'lemon.views.lemon_list'),
    #正则圆括号取出来的值传给函数lemon_update.依次类推
    url(r'^blog_update/(\d+)$', 'lemon.views.lemon_update'),
    url(r'^delete/(\d+)$', 'lemon.views.lemon_delete'),

                       
    url(r'^admin/', include(admin.site.urls)),
    
)
