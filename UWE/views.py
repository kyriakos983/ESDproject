from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from .forms import MovieForm
from UWE.models import TicketDiscount
from UWE.models import Movies


def Home(request):
    context = {}
    return render(request, 'home.html', context)


def about_us(request):
    context = {}
    return render(request, 'aboutus.html', context)


# view the student view
def MoviesView(request):
    movies = Movies.objects.all()
    context = {'movies': movies}
    return render(request, 'films.html', context)


def DiscountView(request):
    discounts = TicketDiscount.objects.all()
    context = {'discounts': discounts}
    return render(request, 'offersAndDiscounts.html', context)


# this is for cinema manager
def add_movie(request):
    form = MovieForm
    if request.method == 'POST:':
        image = request.POST['image']
        name = request.POST['username']
        screen = request.POST['screen']
        dateAndTime = request.POST['dateAndTime']
        ticketPrice = request.POST['ticketPrice']
        movieObject = Movies(image=image, name=name, screen=screen, dateAndTime=dateAndTime, ticketPrice=ticketPrice)
        movieObject.save()
    context = {'form': form}
    return render(request, 'addFilm.html', context)


# this is for cinema manager
def delete_movie(request):
    form = MovieForm
    if request.method == 'POST:':
        image = request.POST['image']
        name = request.POST['username']
        screen = request.POST['screen']
        dateAndTime = request.POST['dateAndTime']
        ticketPrice = request.POST['ticketPrice']
        movieObject = Movies(image=image, name=name, screen=screen, dateAndTime=dateAndTime, ticketPrice=ticketPrice)
        movieObject.save()
    context = {'form': form}
    return render(request, 'delete.html', context)
