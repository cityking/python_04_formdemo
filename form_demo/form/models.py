# coding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=20, verbose_name='名称')
    class Meta:
        verbose_name = u'书籍'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'名称')
    class Meta:
        verbose_name = u'分类信息'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'姓名')
    email = models.EmailField(verbose_name=u'邮箱')
    message = models.TextField(verbose_name=u'内容')
    subject = models.ForeignKey(Category, verbose_name=u'分类名称')
    book = models.ManyToManyField(Book, verbose_name=u'喜欢的书籍')
    class Meta:
        verbose_name = u'我的邮件'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name


