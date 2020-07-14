"""laboref URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from applications.animal.urls import animal_patterns
from applications.core.urls import core_patterns
from applications.adoptions.urls import adoptions_patterns
from applications.blog.urls import blog_patterns
from applications.contacts.urls import contacts_patterns
from applications.about.urls import about_patterns
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core_patterns)),
    path('animal/', include(animal_patterns)),
    path('adoptions/', include(adoptions_patterns)),
    path('blog/', include(blog_patterns)),
    path('contacts/', include(contacts_patterns)),
    path('about/', include(about_patterns)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)