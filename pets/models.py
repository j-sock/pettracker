from django.db import models
from django.contrib.auth.models import User

from datetime import datetime, date

from PIL import Image

SEX_CHOICES = (
	('FF', 'Female'),
	('FS', 'Female (Spayed)'),
	('MM', 'Male'),
	('MN', 'Male (Neutered)'),
)


class Animal(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	icon = models.ImageField(upload_to='icons/animals')

	def __unicode__(self):
		return '{}'.format(self.name)


class Human(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100, default='')
	icon = models.ImageField(upload_to='icons/humans')

	def __unicode__(self):
		return '{}'.format(self.user.username + ": " + self.name)


class Pet(models.Model):
	# profile
	name = models.CharField(max_length=100, default='')
	icon = models.ImageField(upload_to='icons/pets')
	caregivers = models.ManyToManyField(Human, related_name='caregivers')
	friends = models.ManyToManyField('self')

	# breed info
	animal = models.ForeignKey(Animal)
	breed = models.CharField(max_length=100, default='')

	# personal info
	sex = models.CharField(max_length=2, choices=SEX_CHOICES)
	age = models.IntegerField(default=0)
	vets = models.ManyToManyField(Human, blank=True, null=True, related_name='vets')
	health_notes = models.TextField(blank=True, null=True)

	# fun
	about = models.TextField(blank=True, null=True)
	likes = models.TextField(blank=True, null=True)
	dislikes = models.TextField(blank=True, null=True)
	goals = models.TextField(blank=True, null=True)

	def __unicode__(self):
		return '{}'.format(self.name)


class Task(models.Model):
	name = models.CharField(max_length=100)
	pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
	done = models.BooleanField(default=False)

	def __unicode__(self):
		return '{}'.format(self.name)

