#from django.contrib.auth.forms import UserCreationForm
from users.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect
from django.http import HttpResponse ,HttpResponseRedirect
from users import models
from django.contrib import messages

# Create your views here.

def indexview(request):
    return render(request , "index.html")

def registerView(request):
    if request.method == "POST":

        form = UserCreationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully')
            form.save()
            return redirect('register_url')
    else:
        form  = UserCreationForm()

    return render(request , "registration/register.html" , {'form':form})