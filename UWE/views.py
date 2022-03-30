from django.shortcuts import render, redirect
from .forms import MovieForm
from UWE.models import TicketDiscount
from UWE.models import Movies
from django.db.models import F


def Home(request):
    context = {}
    return render(request, 'home.html', context)

def about_us(request):
    context = {}
    return render(request, 'about_us.html', context)

# view the student view
def MoviesView(request):
    movies = Movies.objects.all()
    context = {'movies': movies}
    return render(request, 'films.html', context)


def DiscountView(request):
    discounts = TicketDiscount.objects.annotate(offer=((F('total_price') - F('sale_price')) / F('total_price')) * 100)
    context = {'discounts': discounts}
    return render(request, 'offersAndDiscounts.html', context)


# this is for cinema manager
def add_movie(request):
    form = MovieForm
    user = request.user
    if user.is_cinema_manager:
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
