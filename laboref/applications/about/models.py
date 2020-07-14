from django.db import models
from ckeditor.fields import RichTextField


class Collaborator(models.Model):
    name = models.CharField(max_length=50, default="", verbose_name="Nombre Del Colaborador")
    description = RichTextField(verbose_name="Descripción")
    image = models.ImageField(upload_to="collaborator", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Colaborador"
        verbose_name_plural = "Colaboradores"
        ordering = ['created']

    def __str__(self):
        return self.name
