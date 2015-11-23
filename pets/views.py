from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

import json

from .models import Animal, Pet, CustomTask
from .forms import PetForm, TaskForm, TaskCheckForm

def index(request):
	tasks = CustomTask.objects.order_by('-name')[:5]
	return render(request, 'pets/index.html', {'tasks': tasks})

def list_pets(request):
	pets = Pet.objects.order_by('-name')
	return render(request, 'pets/list_pets.html', {'pets': pets})

def get_pet(request, pk):
	pet = Pet.objects.get(pk=pk)
	return render(request, 'pets/pet.html', {'pet': pet})

def add_pet(request):
	if request.method == 'POST':
		form = PetForm(request.POST, request.FILES)
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
	if request.method =='POST':
		form = TaskCheckForm(request.POST)
		if form.is_valid():
			form.save()
	tasks = CustomTask.objects.filter(pet=pk)
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
		task = get_object_or_404(CustomTask, pk=pk)
		form = TaskForm(instance=task)
	return render(request, 'pets/edit_task.html', {'id': pk, 'pet_id': task.pet.pk, 'form': form})

def do_task(request, pk):
	if request.method == 'POST':
		task = get_object_or_404(CustomTask, pk=pk)
		task.done = request.POST.get('done') == 'true'
		task.save()
		return HttpResponse(json.dumps({'task_name': task.name, 'pet': task.pet.name, 'done': task.done}), content_type="application/json")
	return HttpResponse(json.dumps({'error': 'request wasn not post'}), content_type="application/json")
