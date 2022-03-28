from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

from allAccounts.forms import RegistserUserForm


def register_user(request):
    if request.method == 'POST':
        form = RegistserUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration successul"))
            return redirect('base')
    else:
        form = RegistserUserForm()
    return render(request, 'authenticate/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # redirect to a success page
            return redirect('home')
        else:
            messages.success(request, ("Wrong username or password Check the credentials and Try Again... "))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You were loged out... "))
    return redirect('home')