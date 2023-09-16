from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'authentication/index.html')

def signup(request):
    return render(request, 'authentication/signup.html')

def login_request(request):
    return render(request, 'authentication/login.html')

def logout_request(request):
    pass