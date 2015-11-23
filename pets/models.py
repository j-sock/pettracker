from django.db import models
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


class Species(Animal):
	
	def __unicode__(self):
		return '{}'.format(self.name)


class Breed(Animal):
	species = models.ForeignKey(Species, null=True, on_delete=models.CASCADE)

	def __unicode__(self):
		return '{} ({})'.format(self.name, self.species)


class Pet(models.Model):
	name = models.CharField(max_length=100, default='')
	icon = models.ImageField(upload_to='icons/pets')
	species = models.ForeignKey(Animal)
	sex = models.CharField(max_length=2, choices=SEX_CHOICES)
	birthday = models.DateField()
	notes= models.TextField(null=True)

	def __unicode__(self):
		return '{}'.format(self.name)

	def get_age(self):
		today = date.today()
		return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))


class Task(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return '{}'.format(self.name)


class GenericTask(Task):
	animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

	def __unicode__(self):
		return '{} ({})'.format(self.name, self.animal)


class CustomTask(Task):
	pet = models.ForeignKey(Pet, null=True, on_delete=models.CASCADE)
	done = models.BooleanField(default=False)

	def __unicode__(self):
		return '{}'.format(self.name)

