from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

from todolist.models import Task
from todolist import forms

# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    todo = Task.objects.filter(user=request.user)
    context = {
    'user': request.user,
    'todolist': todo,
    }
    return render(request, "todolist.html", context)

def create_task(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task(user=user, title=title, description=description)
        task.save()
        return HttpResponseRedirect(reverse('todolist:show_todolist'))

    context = {}
    return render(request, 'create_task.html', context)

def change_status(request, id):
    user = User.objects.get(username=request.user)
    task = Task.objects.get(user=user, pk=id)
    task.is_finished = not task.is_finished
    task.save()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

def delete_task(request, id):
    user = User.objects.get(username=request.user)
    task = Task.objects.get(user=user, pk=id)
    task.delete()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))
