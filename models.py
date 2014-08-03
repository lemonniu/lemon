#coding:utf-8

from django.db import models

#为了使用jango系统提供的父类，所以用定义类的方法

class test(models.Model):
	title = models.CharField(max_length=140)
	content = models.TextField()
	create_date = models.DateTimeField(auto_now_add=True)
	#如果不写return函数，在网页上显示test只能是一个一个的object
	#可以用以下方法来取出某个属性来显示即可
	def __unicode__(self):
                return self.title

        

