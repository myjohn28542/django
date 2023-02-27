from django.shortcuts import render
from django.http.response import HttpResponse


def home(request):
    return render(request, 'app_general/home.html')
# Create your views here.


def about(request):
    return render(request, 'app_general/about.html')