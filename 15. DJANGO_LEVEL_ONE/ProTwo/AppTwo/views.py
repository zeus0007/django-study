from django.shortcuts import render
from django.http import HttpResponse
from .models import User


def index(request):
    return render(request, 'AppTwo/index.html')


def help(request):
    helpdict = {'content': 'Help Page'}
    return render(request, 'AppTwo/help.html', helpdict)


def user(request):
    users = User.objects.all()
    user_dict = {'users': users}
    return render(request, 'AppTwo/user.html', user_dict)
