from django.shortcuts import render

from django.http  import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'pages/index.html',  {'name':'michael'})


def about(request):
    return render(request,  'pages/about.html')


def profile(request):
    return render(request, 'pages/profile.html',{'name':'michael'})