from django.db import models
from datetime import date

class Animal(models.Model):
	name = models.CharField(max_length=100, default='')

	def __unicode__(self):
		return '{}'.format(self.name)

class Breed(models.Model):
	name = models.CharField(max_length=100, default='')
	animal = models.ForeignKey(Animal, null=True, on_delete=models.CASCADE)

	def __unicode__(self):
		return '{}'.format(self.name)

class Pet(models.Model):
	name = models.CharField(max_length=100, default='')
	birthday = models.DateField()
	breed = models.ForeignKey(Breed)

	def __unicode__(self):
		return '{}'.format(self.name)

class Task(models.Model):
	name = models.CharField(max_length=100)
	pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
	last_done = models.DateField(null=True)

	def done_today(self):
		return last_done == date.today()

	def __unicode__(self):
		return '{}'.format(self.name)
