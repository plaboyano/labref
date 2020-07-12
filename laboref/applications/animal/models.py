from django.db import models


# tipo de animal

class AnimalType(models.Model):
    animal_type_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Tipo de animal"
        verbose_name_plural = "Tipos de animales"

    def __str__(self):
        return self.animal_type_name


# raza

class Breed(models.Model):
    animal_type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)
    breed_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Raza de animal"
        verbose_name_plural = "Razas"

    def __str__(self):
        return self.breed_name


# color del animal

class AnimalColor(models.Model):
    color_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Color de animal"
        verbose_name_plural = "Color de animales"

    def __str__(self):
        return self.color_name


# animal
class Animal(models.Model):
    animal_name = models.CharField(max_length=255)
    animal_breed = models.ForeignKey(Breed, on_delete=models.DO_NOTHING)
    animal_color = models.ForeignKey(AnimalColor, on_delete=models.DO_NOTHING)
    animal_age = models.IntegerField()
    animal_image = models.ImageField(upload_to='animal/', default='media/None/no-img.jpg')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name_plural = "Animales"
        ordering = ['created']

    def __str__(self):
        return self.animal_name


# animals images
class AnimalImage(models.Model):
    image_description = models.TextField()
    image_url = models.ImageField(upload_to='animal/', default='media/None/no-img.jpg')
    image_animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
