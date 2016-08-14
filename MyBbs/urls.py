"""MyBbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from DjangoUeditor import urls as DjangoUeditor_urls
from Web import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^ueditor/',include('DjangoUeditor.urls' )),
    url(r'^ueditor/',include(DjangoUeditor_urls)),
    url(r'^$',views.index,name='index'),
    url(r'^aritlcelist/$',views.artilce_list,name="aritlcelist"),
    url(r'^category/(\d+)/$',views.category,name="category"),
    url(r'^article/(\d+)/$',views.article_detail,name='article_detail'),
    url(r'^article/new/$',views.new_article,name='new_article'),
    url(r'^account/logout/',views.acc_logout,name='logout'),
    url(r'^account/login/',views.acc_login,name='login'),
    url(r'^test/interface/',views.interface_test,name='interface_test'),
    url(r'^test/interfaceget/',views.interface_get,name='interface_get'),
]
