from django.contrib import admin
from .models import Collaborator


class CollaboratorAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')


admin.site.register(Collaborator, CollaboratorAdmin)
