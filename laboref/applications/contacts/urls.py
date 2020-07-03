from django.urls import path

from .views import IndexView

contacts_patterns = ([
    path('', IndexView.as_view(), name='home'),
    ], 'contacts')
