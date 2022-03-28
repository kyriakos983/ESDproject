from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# view the student form
def Home(request):
    context = {}
    return render(request, 'home.html',context)
