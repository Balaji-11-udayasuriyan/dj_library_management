from tkinter.font import names

from django.urls import path
from . import views
from .views import home, member_register

urlpatterns = [
    path('', views.home, name ='home'),
    path('register/', views.member_register, name ='register'),
    path('dashboard/', views.dashboard, name = 'dashboard')
]