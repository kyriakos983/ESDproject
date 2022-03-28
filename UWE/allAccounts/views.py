from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout





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



def login_view(request):
    form = AuthenticationForm
    if request.method == 'POST':
        username = request.POST.get['username']
        password = request.POST.get['password']
        user = authenticate(username= username, password=password)
        if user is not None and user.is_student:
            login(request,user)
            return redirect('home')
    return render(request, 'authenticate/login.html')
