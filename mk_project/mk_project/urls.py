"""
URL configuration for mk_project project.

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
from mk_app import views

urlpatterns = [
    path('',views.home),
    path('shopnow/',views.shopnow,name="shopnow"),
    path('bikewash/',views.bikewash,name="bikewash"),
    path('carwash/',views.carwash,name="carwash"),
    path('sendmessage/',views.sendmessage,name="sendmessage"),
    path('login/',views.login,name="login"),
    path('shoppingcart/',views.shoppingcart,name="shoppingcart"),
    path('bikeservices/',views.bikeservices,name="bikeservices"),
    path('carservices/',views.carservices,name="carservices"),
    path('monthlyoffer/',views.monthlyoffer,name="monthlyoffer"),
    
]
