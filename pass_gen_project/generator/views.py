import random

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    char_table = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        char_table.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        char_table.extend(list('!@#$%^&*()?<>'))
    if request.GET.get('numbers'):
        char_table.extend(list('0123456789'))
    length = int(request.GET.get('length', 12))
    the_password = ''
    for x in range(length):
        the_password += random.choice(char_table)

    return render(request, 'generator/password.html', {'password': the_password})


def about(request):
    return render(request, 'generator/about.html')
