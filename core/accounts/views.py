from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm 

# Create your views here.
from django.contrib.auth import get_user_model
User = get_user_model()

def home(request):
    return render(request, 'accounts/home.html')

def about(request):
    return render(request, 'accounts/about.html')

def contact(request):
    return render(request, 'accounts/contact.html')

def profile(request):
    return render(request, 'accounts/profile.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)
