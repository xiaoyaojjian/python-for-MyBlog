#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField
# from DjangoUeditor.commands import UEditorEventHandler

# Create your models here.

# class myEventHander(UEditorEventHandler):
#             def on_selectionchange(self):
#                 return """
#                     function getButton(btnName){
#                         var items=%(editor)s.ui.toolbars[0].items;
#                         for(item in items){
#                             if(items[item].name==btnName){
#                                 return items[item];
#                             }
#                         }
#                     }
#                     var btn=getButton("mybtn1");
#                     var selRanage=id_Description.selection.getRange()
#                     btn.setDisabled(selRanage.startOffset == selRanage.endOffset);

                # """
class Article(models.Model):

    """
        帖子表
    """
    title = models.CharField(u'文章标题',max_length=255,unique=True)
    category = models.ForeignKey("Category",verbose_name=u"帖子所属板块")
    head_img = models.ImageField(upload_to="uploads")
    summary = models.CharField(u"描述",max_length=255)
    # content = models.TextField(u'文章内容')
    content = UEditorField(u'文章内容	', height=300, width=1000,
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='besttome', filePath='uploads/files/')
    author = models.ForeignKey("user_profile",verbose_name=u'文章作者')
    publish_date = models.DateTimeField(u'发布日期',auto_now=True)
    hidden = models.BooleanField(u'是否被隐藏',default=True)
    priority = models.IntegerField(u'优先级',default=1000)

    def __unicode__(self):
        return "<%s,author:%s>" %(self.title,self.author)


class Comment(models.Model):

    """
    评论表
    """
    article = models.ForeignKey(Article)
    user = models.ForeignKey("user_profile")
    parent_comment = models.ForeignKey('self',related_name="p_comment",blank=True,null=True)
    comment = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "<%s,user:%s>" %(self.comment,self.user)

class ThumbUp(models.Model):

    """
    点赞表
    """
    article = models.ForeignKey("Article")
    user = models.ForeignKey("user_profile")
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "<user:%s>" %(self.user)

class Category(models.Model):

    """
    板块表
    """
    name = models.CharField(max_length=64,unique=True)
    admin = models.ManyToManyField("user_profile",verbose_name=u'板块管理员')

    def __unicode__(self):
        return self.name

class user_profile(models.Model):

    """
    账号信息表
    """
    user = models.OneToOneField(User)
    name = models.CharField(max_length=32)
    group = models.ManyToManyField("user_group")

    def __unicode__(self):
        return self.name

class user_group(models.Model):

    """
    用户组表
    """
    name = models.CharField(max_length=64,unique=True)

    def __unicode__(self):
        return self.name