from django.shortcuts import render, redirect
from . models import Task, Review
from .forms import TaskForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages


def home(request):
    reviews = Review.objects.all()
    tasks = Task.objects.all()
    context = {'reviews':reviews, 'tasks':tasks}
    return render(request, 'home/index.html', context)


def register(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            auth.login(request, new_user)
            messages.success(request, 'Account Created Successfully!')
            return redirect('home')
    context = {'form':form}
    return render(request, 'home/register.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth_user = auth.authenticate(username = username, password = password)
        if auth_user is not None:
            auth.login(request, auth_user)
            messages.success(request, 'Successfully Loged-In!')
            return redirect('home')
        else:
            messages.error(request, 'User doesn\'t exist!')
    return render(request, 'home/login.html')


def logout(request):
    auth.logout(request)
    messages.success(request, 'Successfully loged-out!')
    return redirect('home')


@login_required
def singleTask(request, pk):
    task = Task.objects.get(id = pk)
    context = {'task':task}
    return render(request, 'home/task_detail.html', context)


@login_required
def createTask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'home/task_create.html', context)


@login_required
def updateTask(request, pk):
    task = Task.objects.get(id = pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect('task-detail', pk = task.id)
    context = {'form':form}
    return render(request, 'home/task_update.html', context)


@login_required
def deleteTask(request, pk):
    task = Task.objects.get(id = pk)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    context = {'task':task}
    return render(request, 'home/task_delete.html', context)