from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if (request.GET.get('uppercase')):
        characters += list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    if (request.GET.get('special')):
        characters += list("!@#$%^&*()")

    if (request.GET.get('numbers')):
        characters += list("0123456789")

    length = int(request.GET.get('password_length', 10))

    generated_password = ""

    for i in range(length):
        generated_password += random.choice(characters)

    return render(request, 'generator/password.html', {'generated_password' : generated_password})

def about(request):

    return render(request, 'generator/about.html')
