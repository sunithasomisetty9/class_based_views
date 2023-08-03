"""
URL configuration for project47 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fbv_string/',fbv_string,name='fbv_string'),
    path('fbv_render/',fbv_render,name='fbv_render'),
    path('CbvString/',CbvString.as_view(),name='CbvString'),
    path('CbvRender/',CbvRender.as_view(),name='CbvRender'),
    path('CbvTemp/',CbvTemp.as_view(),name='CbvTemp'),
    path('fbv_form/',fbv_form,name='fbv_form'),
    path('CbvForm/',CbvForm.as_view(),name='CbvForm'),


    path('render_url/',TemplateView.as_view(template_name='render_url.html'),name='render_url'),

    path('TempDataRender/',TempDataRender.as_view(),name='TempDataRender'),

    path('TempInsertForm/',TempInsertForm.as_view(),name='TempInsertForm'),

    path('FormInsert/',FormInsert.as_view(),name='FormInsert'),

    path('Trainers_List/',Trainers_List.as_view(),name='Trainers_List'),

]
