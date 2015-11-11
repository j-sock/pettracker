from django.contrib import admin

# Register your models here.
from .models import *
 
admin.site.register(Animal)
admin.site.register(Breed)
admin.site.register(Pet)
admin.site.register(Task)
