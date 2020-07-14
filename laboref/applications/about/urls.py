from django.urls import path

from .views import IndexView

about_patterns = ([
    path('', IndexView.as_view(), name='home'),
    ], 'about')
