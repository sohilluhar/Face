"""Face URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from Face import view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('verifyuser',view.verify,),
    # path('home',view.home),
    url(r'^verifyuser$',view.verify,name="verify_user"),
    url(r'^home$',view.home,name="home"),
    url(r'^detect_criminal$',view.detect_criminal,name="detect_criminal"),
    url(r'^test$',view.test,name="test"),

    path('',view.login),
]
