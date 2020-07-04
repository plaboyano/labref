from django.urls import path

from .views import AboutView, ItemSliderListView

core_patterns = ([
    path('', ItemSliderListView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about')
    ], 'core')
