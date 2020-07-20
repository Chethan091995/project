from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("hello world")
def demo(request):
    return render(request,"demo1.html")
def demo2(request):
    return render(request,"directory/demo2.html")