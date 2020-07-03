from django.urls import path

from .views import IndexView

blog_patterns = ([
    path('', IndexView.as_view(), name='home'),
    ], 'blog')
