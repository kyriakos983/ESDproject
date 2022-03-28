from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# view the student form
from UWE.forms import addmovieForm
from UWE.models import Movies


def Home(request):
    context = {}
    return render(request, 'home.html',context)

def MoviesView(request):
    movies = Movies.objects.all()
    context = {'movies':movies}
    return render(request, 'films.html', context)

# this is for cinema manager
def addMoviePage(request):
    form = addmovieForm
    #if method is post to send data into database save all the inforamtion in the profile model
    if request.method == 'POST':
        if request.user.is_authenticated:
            name = request.POST['name']
            screen = request.POST['screen']
            dateAndTime = request.POST["dateAndTime"]
            ticketPrice = request.POST['ticketPrice']
            image = request.POST['image']
            MovieObject = Movies(name=name, screen=screen,dateAndTime=dateAndTime,ticketPrice=ticketPrice,image=image)
            MovieObject.save()
        #print(user,first_name,last_name,preference,condition)

    context = {'form':form}
    return render(request,'templates/addFilm.html',context)

