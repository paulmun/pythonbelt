from django.shortcuts import render, redirect
from . import models
from django.db.models import Count
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def index(request):
	user_id = request.session['user']
	user = models.Users.objects.get(id=user_id)	
	pokers = models.Pokes.objects.pokers(user_id)
	pokees = models.Users.objects.everyoneElse(id=user_id)
	
	context={'user':user,'pokees':pokees, 'pokers':pokers, 'total_poked':pokers.count}
	return render(request, 'poke/index.html', context)

def poke(request, pokedID):
	models.Pokes.objects.poke(poker_id=request.session['user'], pokee_id=pokedID)
	messages.success(request,"You poked "+str(pokee.fname)+"!")
	return redirect(reverse('poke:poke_index'))