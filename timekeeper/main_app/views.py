from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm
from .models import Settings


def index(request):
    return render(request, 'index.html', {})


def user_login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('personal')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Settings.objects.create(owner=new_user)
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})


@login_required
def user_personal(request):
    username = request.user.username
    return render(request, 'personal.html', {'username': username})


@login_required
def user_settings(request):
    username = request.user.username
    return render(request, 'settings.html', {'username': username})


@login_required
def user_reports(request):
    username = request.user.username
    return render(request, 'reports.html', {'username': username})


@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

