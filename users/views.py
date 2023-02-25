from django.shortcuts import redirect, render
from events.models import Event

from users.models import Account
from .forms import LogInForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def register_user(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User account was created!')
            login(request, user)
        else:
            messages.error(request, f'An error has occurred during registration')

    context = {'form': form}
    return render(request, 'users/register.html', context)


def login_user(request):

    if request.user.is_authenticated:
        return redirect('home')

    form = LogInForm()
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'home')
        else:
            messages.error(request, 'Username OR password is incorrect')

    context = {'form': form}
    return render(request, 'users/login.html', context)


def logout_user(request):
    logout(request)
    messages.info(request, 'logged out!')
    return redirect('login')


@login_required(login_url='login')
def profile(request):
    print(request.user)
    events = Event.get_user_events(request.user)
    context = {'events': events}
    return render(request, 'users/profile.html', context)
