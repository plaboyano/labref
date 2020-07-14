from django.contrib import admin
from .models import ItemSlider, News, Welcome


class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')


admin.site.register(ItemSlider)
admin.site.register(Welcome)
admin.site.register(News, HomeAdmin)
