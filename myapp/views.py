from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, StudentForm
from django.contrib import messages
from .models import *

from django.contrib.auth import authenticate, login as auth_login, logout
# Create your views here.
def home(request):
	return render(request,'myapp/home.html')

def register(request):
	form=RegisterForm()
	if request.method=="POST":
		form=RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,f'Register Success')
			return redirect('register')
	context={'form':form}
	return render(request,'myapp/register.html', context)

def loginuser(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']

		user=authenticate(request, username=username, password=password)
		if user is not None:
			auth_login(request, user)
			return redirect('/add_show')
		else:
			messages.info(request,'Username or Password is incorrect')
	return render(request,'myapp/login.html')

def logoutuser(request):
	logout(request)
	return redirect('/')

def showdetails(request):
	std=Student.objects.all()
	form=StudentForm()
	if request.method=="POST":
		form=StudentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('add_show')
	context={'form':form,'std':std}
	return render(request,'myapp/add_show.html',context)


def updatedetails(request, pk):
	std=Student.objects.get(id=pk)
	form=StudentForm()
	if request.method=="POST":
		form=StudentForm(request.POST, instance=std)
		if form.is_valid():
			form.save()
			return redirect('add_show')
	context={'form':form, std:std}
	return render(request,'myapp/update.html', context)

def delete(request,pk):
	std=Student.objects.get(id=pk)
	if request.method=="POST":
		std.delete()
		return redirect('add_show')