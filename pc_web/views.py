#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'pc/home.html')


def add(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))