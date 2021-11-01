from django.contrib.auth import authenticate, login, get_user_model
from django.core.checks.messages import Error
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import LoginForm,RegistrationForm

User = get_user_model()

def register(request):
    form = RegistrationForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        firstname = form.cleaned_data.get("firstname")
        lastname = form.cleaned_data.get("lastname")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create(username=username,email=email,
                                        first_name=firstname,last_name=lastname,password=password)
        
        login(request,new_user)
        print("created and logged in")
    
    return render(request,template_name="auth/register.html",context=context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None and user.is_authenticated:
            print("user is authenticated")
            login(request,user)
            redirect("/caterer/")
        else:
            print(Error)

    return render(request,"auth/login.html",context=context)    
