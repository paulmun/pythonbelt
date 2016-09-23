from __future__ import unicode_literals
from django.db import models
from ..logreg.models import Users
from django.db.models import Count

class PokesManager(models.Manager):
	def poke(self, poker_id, pokee_id):
		poker = self.get(id=poker_id)
		pokee = self.get(id=pokee_id)

		newPoke = self.create(poker=poker, pokee=pokee)
		return newPoke

	def pokers(self, id):
		pokers = Users.objects.filter(poker__pokee__id=id).annotate(number=Count('poker__pokee')).order_by('-number')
		return pokers

class Pokes(models.Model):
	poker = models.ForeignKey(Users, related_name='poker')	
	pokee = models.ForeignKey(Users, related_name='pokee')
	created_at = models.DateTimeField(auto_now_add=True)
	objects=PokesManager()
