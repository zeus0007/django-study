from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<em>My Second Project</em>")


def help(request):
    helpdict = {'content': 'Help Page'}
    return render(request, 'AppTwo/help.html', helpdict)
