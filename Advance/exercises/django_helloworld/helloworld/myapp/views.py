from django.shortcuts import render
from django.http import HttpResponse

def mainpage(request):
    return HttpResponse("اولین صفحه‌ی من")
