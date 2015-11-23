from django import forms
from pets.models import Pet, CustomTask

class PetForm(forms.ModelForm):

	class Meta:
		model = Pet
		fields = '__all__'


class TaskForm(forms.ModelForm):

	class Meta:
		model = CustomTask
		fields = ['name', 'pet']


class TaskCheckForm(forms.ModelForm):

	class Meta:
		model = CustomTask
		fields = ['name', 'pet', 'done']