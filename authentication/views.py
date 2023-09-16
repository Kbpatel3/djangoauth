from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'authentication/index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']


    return render(request, 'authentication/signup.html')

def login_request(request):
    return render(request, 'authentication/login.html')

def logout_request(request):
    pass