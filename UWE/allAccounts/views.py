from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
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
