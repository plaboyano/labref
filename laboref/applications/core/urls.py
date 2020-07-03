from django.urls import path

from .views import IndexView, AboutView

core_patterns = ([
    path('', IndexView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about')
    ], 'core')
