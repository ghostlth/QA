#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class Question(models.Model):
    STATUS_CHOICE = (
        ('0','未提交'),
        ('1','未处理'),
        ('2','已处理')
    )
    TYPE_CHOICE = (
        ('0','电脑问题'),
        ('1','OA系统问题'),
        ('2','NC系统问题'),
        ('3','账号密码重置')
    )
    questionTitle = models.CharField('问题标题',max_length=256)
    createTime = models.DateTimeField('创建时间',auto_now_add=True)
    endTime = models.DateTimeField('结束时间',auto_now=True)
    questionDescription = models.TextField('问题描述',default='')
    status = models.CharField('问题状态',max_length=1,choices=STATUS_CHOICE,default='0')
    questionType = models.CharField('问题分类',max_length=1,choices=TYPE_CHOICE,default='0')

    def __str__(self):
        return self.questionTitle



class Document(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE,verbose_name='文档来源')
    releaseTime = models.DateTimeField('发布时间',auto_now=True)


    def __str__(self):
        return self.question