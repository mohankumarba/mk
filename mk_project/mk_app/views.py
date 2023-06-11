from django.shortcuts import render
from django.http import HttpResponse
from .models import set
def home(request):
    return render(request,'mk.html')
def shopnow(request):
    return render(request,'shopnow.html')
def bikewash(request):
    return render(request,'bikewash.html')
def carwash(request):
    return render(request,'carwash.html')
def sendmessage(request):
    return render(request,'sendmessage.html')
def login(request):
    return render(request,'login.html')
def shoppingcart(request):
    return render(request,'shoppingcart.html')
def bikeservices(request):
    return render(request,'bikeservices.html')
def carservices(request):
    return render(request,'carservices.html')
def monthlyoffer(request):
    return render(request,'monthlyoffer.html')
# Create your views here.
