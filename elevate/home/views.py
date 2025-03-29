from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home/index.html')

def register(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            auth.login(request, new_user)
            messages.success(request, 'Account Created Successfully!')
            return redirect('dashboard')
    context ={'form':form}  
    return render(request, 'home/register.html', context)

def login(request):
    if request.user.is_authenticated:
        messages.info(request, "You've already Loged-in!")
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth_user = auth.authenticate(username = username, password = password)
        if auth_user is not None:
            auth.login(request, auth_user)
            messages.success(request, 'Successfully Loged-in!')
            return redirect('dashboard')
        else:
            messages.error(request, "User doesn't Exist!")
            return redirect('login')
    return render(request, 'home/login.html')

def logout(request):
    if not(request.user.is_authenticated):
        messages.info(request, "You've not Logged-in!")
        return redirect('home')
    auth.logout(request)
    messages.success(request, 'Successfully Loged-out!')
    return redirect('home')

@login_required
def dashboard(request):
    return render(request, 'home/dashboard.html')



