from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.views import generic

import json

from .models import Animal, Human, Pet, Task
from .forms import PetForm, HumanForm, TaskForm, TaskCheckForm

## actual pages

# log in
def log_in(request):
	if request.method == 'POST':
		username = request.POST['username']
    	password = request.POST['password']
    	user = authenticate(username=username, password=password)
    	if user is not None:
	        if user.is_active:
	        	login(request, user)
	        	return HttpResponseRedirect('/')
	return render(request, 'pets/login.html')

# home page
def index(request):
	if(request.user.username != ''):
		user = Human.objects.get(user=request.user.id)
		pets = Pet.objects.filter(caregivers__id=user.pk)
		tasks = Task.objects.order_by('-name')[:5]
		return render(request, 'pets/index.html', {'user': user, 'tasks': tasks, 'pets': pets})
	return render(request, 'pets/login.html')

# pet profile
def get_pet(request, pk):
	pet = Pet.objects.get(pk=pk)
	return render(request, 'pets/pet.html', {'pet': pet})

# task list
def get_tasks(request):
	if(request.user.username != ''):
		user = Human.objects.get(user=request.user.id)
		pets = Pet.objects.filter(caregivers__id=user.pk)
		tasks = []
		for pet in pets:
			tasks += Task.objects.filter(pet=pet.pk)
		return render(request, 'pets/tasks.html', {'user': user, 'tasks': tasks, 'pets': pets})
	return render(request, 'pets/login.html')


## do things

# log out
def log_out(request):
	logout(request)
	return render(request, 'pets/login.html')

# check off task
def do_task(request, pk):
	if request.method == 'POST':
		task = get_object_or_404(Task, pk=pk)
		task.done = request.POST.get('done') == 'true'
		task.save()
		return HttpResponse(json.dumps({'task_name': task.name, 'pet': task.pet.name, 'done': task.done}), content_type="application/json")
	return HttpResponse(json.dumps({'error': 'request wasn not post'}), content_type="application/json")

###########

def get_human(request, pk):
	human = Human.objects.get(pk=pk)
	pets = Pet.objects.filter(caregivers__id=pk)
	tasks = []
	for pet in pets:
		tasks += Task.objects.filter(pet__id=pet.pk)
	return render(request, 'pets/human.html', {'human': human, 'pets': pets, 'tasks': tasks})	

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
	print "edit task"
	if request.method == 'POST':
		task = get_object_or_404(Task, pk=pk)
		task.name = request.POST.get('name')
		task.pet = Pet.objects.get(pk=request.POST.get('pet'))
		task.save()
		return HttpResponseRedirect('/tasks')
	else:
		task = get_object_or_404(Task, pk=pk)
		form = TaskForm(instance=task)
	return render(request, 'pets/edit_task.html', {'id': pk, 'pet_id': task.pet.pk, 'form': form})


