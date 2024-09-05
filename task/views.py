from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1 style='display:flex;justify-content:center;'>Welcome to Django Task</h1>")

