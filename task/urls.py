from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about_me/', views.about_me, name='about_me'),
    path('contact_us/', views.contact_us, name='contact_us'),
]
