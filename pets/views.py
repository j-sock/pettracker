from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Pet, Task
from .forms import PetForm , TaskForm

def index(request):
	pets = Pet.objects.order_by('-name')
	return render(request, 'pets/index.html', {'pets': pets})


class IndexView(generic.ListView):
	template_name = 'pets/index.html'
	context_object_name = 'pets'

	def get_queryset(self):
		return Pet.objects.order_by('-name')


class DetailView(generic.DetailView):
	model = Pet
	template_name = 'pets/detail.html'

def get_pet(request, pk):
	pet = Pet.objects.get(pk=pk)
	return render(request, 'pets/pet.html', {'pet': pet})

def add_pet(request):
	if request.method == 'POST':
		form = PetForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/pets/')
	else:
		form = PetForm()
	return render(request, 'pets/add_pet.html', {'form': form})

def edit_detail(request, pk):
	if request.method == 'POST':
		form = PetForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		pet = get_object_or_404(Pet, pk=pk)
		form = PetForm(instance=pet)
	return render(request, 'pets/edit_detail.html', {'id': pk, 'form': form})

def get_tasks(request, pk):
	tasks = Task.objects.filter(pet=pk)
	return render(request, 'pets/tasks.html', {'id': pk, 'tasks': tasks})

def add_task(request):
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/pets/%s/tasks' % request.POST.get('pet'))
	else:
		form = TaskForm()
	return render(request, 'pets/add_task.html', {'form': form})

def edit_task(request, pk):
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/pets/%s/tasks' % request.POST.get('pet'))
	else:
		task = get_object_or_404(Task, pk=pk)
		form = TaskForm(instance=task)
	return render(request, 'pets/edit_task.html', {'id': pk, 'pet_id': task.pet.pk, 'form': form})