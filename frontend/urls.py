from tkinter.font import names

from django.urls import path
from .views import home, member_register, fines_view, dashboard, member_login, member_logout

urlpatterns = [
    path('', home, name ='home'),
    path('register/', member_register, name ='register'),
    path('login/', member_login, name= 'login'),
    path('logout/', member_logout, name='logout'),
    path('dashboard/', dashboard, name = 'dashboard'),

]