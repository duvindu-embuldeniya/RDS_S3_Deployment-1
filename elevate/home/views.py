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
            return redirect('home')
    context ={'form':form}
    return render(request, 'home/register.html', context)

def login(request):
    return render(request, 'home/login.html')

def logout(request):
    pass

@login_required
def dashboard(request):
    return render(request, 'home/dashboard.html')



