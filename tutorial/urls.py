"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from course.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',IndexListView.as_view()),
    #path('index',ajax_method,name="ajax")
    path('',RevisorListView.as_view(),name='revisor_list'),
    path('add/',revisor_create.as_view(), name='revisor_create'),
    path('update/<int:pk>',revisor_update.as_view(), name='revisor_update'),
    path('delete/<int:pk>',revisor_delete.as_view(), name='revisor_delete'),

    
] 

