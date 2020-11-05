from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import RegisterForm, LoginForm, SalaryForm
from .models import Civil_servant, RegistrationData



# Create your views here.

def register(request):
   
    context = {"form": RegisterForm}
  
    return render(request, "register.html", context)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
    
                #name= form.cleaned_data['name'],
                username= form.cleaned_data['username'],
                #email=form.cleaned_data['email'],
                password= form.cleaned_data['password'],  
            
        return HttpResponseRedirect('/login/')

    else:
        form =LoginForm()

    return render(request, "login.html", {'form':form})

   


def home(request):
    return render (request, 'home.html')

def about(request):
    return render (request, 'about.html')


def salary(request):
    #if request.method == 'POST':
    form = SalaryForm(request.POST)

    if form.is_valid():
            salo = form.cleaned_data['salary']
            salo.save()


    return render (request, 'salary.html', {'form' : form});




