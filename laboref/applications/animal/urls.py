from django.urls import path

from .views import IndexView, detail_animal_view, edit_animal_view, new_animal_view

animal_patterns = ([
	path('', IndexView.as_view(), name='index'),
	path('<int:animal_id>/', detail_animal_view, name="detail_animal"),
	path('edit/<int:animal_id>/', edit_animal_view, name="edit_animal"),
	path('new/', new_animal_view, name="new_animal"),
], 'animal')

