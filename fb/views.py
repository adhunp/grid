from django.shortcuts import render

# Create your views here.

def grid(request):
    return render (request,'grid.html')

def adhun(request):
    return render (request,'adhun.html')
