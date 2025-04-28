from django.contrib.auth import login
from django.shortcuts import render, redirect

from frontend.forms import RegisterForm


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

def dashboard(request):
    return render(request, "frontend/auth/dashboard.html")