from django.contrib import admin

# Register your models here.
from .models import *
 
admin.site.register(Species)
admin.site.register(Breed)
admin.site.register(Pet)
admin.site.register(GenericTask)
admin.site.register(CustomTask)
