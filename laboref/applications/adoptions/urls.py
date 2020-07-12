from django.urls import path
from .views import IndexListView

adoptions_patterns = ([
    path('', IndexListView.as_view(), name='home'),
    ], 'adoptions')
