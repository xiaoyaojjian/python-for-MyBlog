#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import forms
import os
# from  DjangoUeditor.forms import UEditorField,UEditorWidget

class ArticleForm(forms.Form):

    title = forms.CharField(max_length=255,min_length=5)
    summary = forms.CharField(max_length=255,min_length=5)
    category_id = forms.IntegerField()
    head_img = forms.ImageField()
    content = forms.CharField(min_length=10)
    # Description=UEditorField("描述",initial="abc",width=600,height=800)
    # Content=forms.CharField(label="内容",widget=UEditorWidget(width=800,height=500))


def handle_uploaded_file(request,f):

    print("--->",f.name)
    base_img_upload_path = 'statics/imgs'
    user_path = '%s/%s' %(base_img_upload_path,request.user.id)
    if not os.path.exists(user_path):
        os.mkdir(user_path)
    with open('%s/%s'%(user_path,f.name),'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return '/static/imgs/%s/%s'%(request.user.id,f.name)