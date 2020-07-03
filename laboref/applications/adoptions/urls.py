from django.urls import path
from .views import IndexView

adoptions_patterns = ([
    path('', IndexView.as_view(), name='home'),
    ], 'adoptions')
