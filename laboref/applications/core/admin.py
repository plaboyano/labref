from django.contrib import admin
from .models import ItemSlider, News


class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')


admin.site.register(ItemSlider)
admin.site.register(News, HomeAdmin)
