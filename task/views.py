from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1 style='display:flex;justify-content:center;'>Welcome to Django Task</h1>")


def about_me(request):
    company_info = {
        'company_name': 'Coding Company',
        'address': '10 Horabi street',
        'phone': '+123456789',
        'email': 'code@gmail.com',
        'image': 'static/img/photo.png',
    }
    
    return render(request, 'task/about_me.html', {'company_info': company_info})


def contact_us(request):
    return render(request, 'task/contact_us.html')
