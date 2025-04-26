from django.shortcuts import render
from .models import AuthorUser, Category


def dashboard_callback(request, context):
    author_count = AuthorUser.objects.count()

    context.update({
        "author_count": author_count,
        "custom_message": "welcome to the admin",
    })

    return context

def category_badge_callback(request):
    return Category.objects.count()
