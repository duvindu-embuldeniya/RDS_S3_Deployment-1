from django.shortcuts import render
from . models import Task, Review

def home(request):
    query = Review.objects.filter(reviewer_name = 'duvindu')
    context = {'query':query}

    return render(request, 'home/index.html', context)