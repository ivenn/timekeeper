from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


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
                    return redirect('main')
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


@login_required
def user_main(request):
    username = request.user.username
    return render(request, 'main.html', {'username': username})


@login_required
def user_settings(request):
    username = request.user.username
    return render(request, 'settings.html', {'username': username})


@login_required
def user_reports(request):
    username = request.user.username
    return render(request, 'reports.html', {'username': username})
