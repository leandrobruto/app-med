from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return render(request, 'home.html')

def Login(request):
    return render(request, 'login.html')