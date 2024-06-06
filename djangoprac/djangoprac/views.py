from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello this is the home page from the django")

def htmlpage(request):
    return render(request,"index.html")