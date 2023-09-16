from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'authentication/index.html')

def signup_request(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']

        # Use Django's built-in User model to create a new user
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = first_name
        myuser.last_name = last_name

        # Save the User object
        myuser.save()

        # Show a success message
        messages.success(request, "Your account has been successfully created")

        # Redirect to the login page
        return redirect('login')


    return render(request, 'authentication/signup.html')

def login_request(request):
    if request.method == 'POST':
        # Get the post parameters
        login_username = request.POST['username']
        login_password = request.POST['pass1']

        # Check if the user has entered correct credentials
        user = authenticate(username=login_username, password=login_password)

        # If the user is found
        if user is not None:
            # Log the user in
            login(request, user)
            messages.success(request, "You have successfully logged in")
            return render(request, 'authentication/index.html', {'fname': user.first_name})
        else:
            # Return an error message
            messages.error(request, "Invalid credentials! Please try again")
            return redirect('home')

    return render(request, 'authentication/login.html')

def logout_request(request):
    pass