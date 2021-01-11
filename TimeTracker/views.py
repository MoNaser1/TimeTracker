from django.shortcuts import render, redirect
from .forms import MyCustomSignupForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.
def home(request):
    return render(request, "layout/home.html", {})


def list(request):
    tasks = Post.objects.all()

    form = TaskForm()
    # import pdb
    # pdb.set_trace()
    if request.method == 'POST':

        form = TaskForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()  # saved to the database
            return redirect('/list')
    context = {'tasks': tasks, 'form': form}

    return render(request, "layout/list.html", context)


def updateTask(request, pk):
    task = Post.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/list')
    context = {'form': form}

    return render(request, 'layout/updateTask.html', context)


def deleteTask(request, pk):
    item = Post.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/list')
    context = {'item': item}
    return render(request, 'layout/deleteTask.html', context)


def start_time(request, pk):
    sTime = Post.objects.get(pk=id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'startTime': sTime,
        'form': form}

    return render(request, 'layout/list.html', context)


def end_time(request, pk):
    eTime = Post.objects.get(pk=id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'endTime': eTime,
        'form': form}

    return render(request, 'layout/list.html', context)


# def employee(request, pk):
#     emp = Post.objects.get(pk=id)
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context = {
#         'employee': emp,
#         'form': form}
#
#     return render(request, 'layout/list.html', context)

def signup(request):
    if request.methods == 'POST':
        form = MyCustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/accounts/profile')
    else:
        form = MyCustomSignupForm()

    return render(request, 'account/signup.html', {'form': form})
