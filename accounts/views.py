from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect,reverse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required


def register(request):
    form=CustomUserCreationForm()
    if request.method== 'POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print('user succefully created')
            return redirect(reverse('home'))
    return render(request,'accounts/register.html',{'form':form})



def logout(request):
    auth.logout(request)
    return redirect('/')
