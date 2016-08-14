#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate,login,logout
from forms import ArticleForm,handle_uploaded_file
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# from DjangoUeditor.forms import UEditorField

# Create your views here.

def page_show(request,show,n):
    '''
    分页功能，接受三个参数，请求，显示功能模块，每页显示多少
    :param show:
    :param n:
    :return:
    '''

    paginator = Paginator(show,n)
    page_count = paginator.count
    # 分页
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        #如果页面数据为空
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return contacts,page_count

def index(request):

    """
        首页显示所有内容
    :param request:
    :return:
    """
    articles = models.Article.objects.all()
    #分页
    # paginator = Paginator(articles,5)
    # page = request.GET.get('page')
    # try:
    #     contacts = paginator.page(page)
    # except PageNotAnInteger:
    #     #如果页面数据为空
    #     contacts = paginator.page(1)
    # except:
    #     contacts = paginator.page(paginator.num_pages)
    username = request.session.get('username','')
    print username
    articles,page_count = page_show(request,articles,5)
    return render(request,'index.html',{'articles':articles,'username':username,'page_count':page_count})



def artilce_list(request):

    """
        首页显示所有内容
    :param request:
    :return:
    """
    articles = models.Article.objects.all()

    return render(request,'articlelist.html',{'articles':articles})

def category(request,category_id):

    # print '>>',category_id
    articles = models.Article.objects.filter(category_id=category_id)
    articles,page_count = page_show(request,articles,5)
    return render(request,'index.html',{'articles':articles,'page_count':page_count})

def article_detail(request,article_id):

    try:

        article_obj = models.Article.objects.get(id=article_id)
    except ObjectDoesNotExist as e:
        return render(request,"404.html",{'err_msg':u'文章不存在！'})
    return render(request,'article.html',{'article_obj':article_obj})

def acc_logout(request):

    logout(request)
    response = HttpResponseRedirect('/')
    # response.delete_cookie('username')
    #清除用户session
    # del request.session['username']
    # return HttpResponseRedirect('/')
    return response

def acc_login(request):

    print(request.POST)
    err_msg = ''
    if request.method == 'POST':
        print ('user authention .....')
        # username = request.POST.get('username')
        username = request.POST.get('username')
        password = request.POST.get('password')
        print username,password
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            response = HttpResponseRedirect('/')
            # response.set_cookie('username',username,3600)
            #将session信息写到服务器
            request.session['username'] = username
            # return HttpResponseRedirect('/')
            return response
        else:
            err_msg = 'Wrong username or password!'

    return render(request,'login.html',{'err_msg':err_msg})

def new_article(request):


    if request.method == 'POST':
        print(request.POST)
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            print('---form.data:',form.cleaned_data)
            form_data = form.cleaned_data
            print(form_data,request.user.id)
            form_data['author_id'] = request.user.id
            print(form_data)

            new_img_path = handle_uploaded_file(request,request.FILES['head_img'])
            form_data['head_img'] = new_img_path
            print (form_data)
            new_article_obj = models.Article(**form_data)
            new_article_obj.save()
            return render(request,'new_article.html',{'new_article_obj':new_article_obj})
        else:
            print('err:',form.errors)
    category_list = models.Category.objects.all()
    return render(request,'new_article.html',{'category_list':category_list})

def interface_test(request):

    return render(request,'interface_test.html',{'interface_test':interface_test})

def interface_get(request):

    return render(request,'interface_get.html',{'interface_get':interface_get})
