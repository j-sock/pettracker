from django import forms
from pets.models import Pet, Human, Task

class PetForm(forms.ModelForm):

	class Meta:
		model = Pet
		fields = '__all__'


class HumanForm(forms.ModelForm):

	class Meta:
		model = Human
		fields = '__all__'


class TaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ['name', 'pet']


class TaskCheckForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ['name', 'pet', 'done']