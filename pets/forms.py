from django import forms
from pets.models import Pet, Task

class PetForm(forms.ModelForm):

	class Meta:
		model = Pet
		fields = '__all__'


class TaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ['name', 'pet']