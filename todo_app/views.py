from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"todo_app/index.html")

def about(request):
    return render(request,"todo_app/about.html")

def create(request):
    return render(request,"todo_app/create.html")
