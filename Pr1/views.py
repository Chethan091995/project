from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("hello world")
def demo(request):
    return render(request,"demo1.html")
def demo2(request):
    return render(request,"directory/demo2.html")
def first(request):
    return render(request,"first.html",context={'data':'Python','name':'Chethan'})
def second(request):
    fruits=["apple","mango","banana"]
    return render(request,"directory/second.html",context={"fruits":fruits})
def greater(request):
    return render(request,"directory/greater.html",context={"a":10,"b":20})