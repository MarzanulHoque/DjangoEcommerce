from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse("we are at about page")

def contact(request):
    return HttpResponse("we are at contact page")

def tracker(request):
    return HttpResponse("we are at tracker page")

def search(request):
    return HttpResponse("we are at search page")

def productView(request):
    return HttpResponse("we are at productView page")

def checkout(request):
    return HttpResponse("we are at checkout page")