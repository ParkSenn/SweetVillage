from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from account.forms import UserForm

def login(request):
    if request.method == 'POST':
        usr = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=usr, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('quizeapp:new')
        else:
            return render(request, 'login.html')
    elif request.method == 'GET':
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('quizeapp:new')


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user=authenticate(username=username,password=raw_password)
            auth.login(request,user)
            return redirect('quizeapp:new')

    else:
        form = UserForm()
    return render(request, 'signup.html',{'form':form}
    )       
