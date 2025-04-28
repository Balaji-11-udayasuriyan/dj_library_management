from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from backend.models import Fine
from frontend.forms import RegisterForm, LoginForm


# Create your views here.
def home(request):
    return render(request, "frontend/home.html")

# Member Registration
def member_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'frontend/auth/register.html', {'form': form})


def member_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('member_dashboard')
    else:
        form = LoginForm()
    return render(request, 'frontend/login.html', {'form': form})


# Logout
def member_logout(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, "frontend/auth/dashboard.html")

@login_required
def fines_view(request):
    fines = Fine.objects.filter(member=request.user)
    return render(request, 'frontend/fines.html', {'fines': fines})
