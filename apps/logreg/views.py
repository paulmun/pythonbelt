from django.shortcuts import render, redirect
from . import models
from django.contrib import messages

# Create your views here.
def index(request):
	context={'users': models.Users.objects.all()}
	return render(request, 'logreg/index.html', context)

def register(request):
	fname = request.POST['fname']
	lname = request.POST['lname']
	email = request.POST['email']
	newUser = models.Users.objects.register(fname=fname, lname=lname, email=email, password=request.POST['pass'], cpassword=request.POST['cPass'])
	if newUser[0]:
		return redirect('/')
	else:
		context = {'errors':newUser[1], 'fname':fname, 'lname':lname, 'email':email}
		return render(request, 'logreg/index.html', context)

def login(request):
	user = models.Users.objects.login(email=request.POST['email'], password=request.POST['pass'])
	if user[0]:
		request.session['user'] = user[1]
		return render(request, 'logreg/profile.html')
	else:
		context = {'errors2':user[1]}
		return render(request, 'logreg/index.html', context)