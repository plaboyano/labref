from django.contrib import admin
from .models import AnimalType, Breed, AnimalColor, Animal


admin.site.register(Animal)
admin.site.register(AnimalType)
admin.site.register(Breed)
admin.site.register(AnimalColor)
