from django.urls import path
from . import views
from .views import show_name

urlpatterns = [
    path('', views.show_name, name ='show_name')
]