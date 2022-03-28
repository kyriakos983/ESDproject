from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# view the student form
from UWE.models import Movies


def Home(request):
    context = {}
    return render(request, 'home.html',context)

def MoviesView(request):
    movies = Movies.objects.all()
    context = {'movies':movies}
    return render(request, 'films.html', context)