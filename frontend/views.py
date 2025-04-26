from django.shortcuts import render

# Create your views here.
def show_name(request):
    return render(request, 'frontend/show_name.html', {'name': 'John'})

