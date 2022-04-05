from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView

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
# !!!!!!!!! NEEDS TO BE FIXED!!!!!!!!! #
def add_movie(request):
    form = MovieForm(request.POST)
    if request.method == 'POST:':
        if form.is_valid():
            name = form.cleaned_data['name']
            screen = form.cleaned_data['screen']
            dateAndTime = form.cleaned_data['dateAndTime']
            ticketPrice = form.cleaned_data['ticketPrice']
            image = form.cleaned_data['image']
            movieObject = Movies( name=name, screen=screen, dateAndTime=dateAndTime, ticketPrice=ticketPrice, image=image)
            movieObject.save()

    context = {'form': form}
    return render(request, 'addFilm.html', context)


# this is for cinema manager
def delete_movie(request):
    movies = Movies.objects.all()
    context = {'movies': movies}
    return render(request, 'delete.html', context)


#update any changes into the movie details.
class UpdateMovieView(UpdateView):
    model = Movies
    fields = '__all__'
    template_name = 'movieDetails.html'
    success_url = reverse_lazy('home')

    def get_absolute_url(selfself):
        return reverse('home')


# this is to get the product details when a user tries to view details of a movie
def movie_details(request,name, id):
    movie = Movies.objects.get(id=id)
    return render(request, 'movieDetails.html', {'movie': movie})