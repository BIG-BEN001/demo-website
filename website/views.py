from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page_view(request):
    return HttpResponse('<h1>Welcome to my home page</h1>')

def about_page_view(request):
    return HttpResponse('<h1>Welcome to my about page</h1>')

def contact_page_view(request):
    return HttpResponse('<h1>Welcome to my contact page</h1>')