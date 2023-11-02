"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from BookTrackerapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', views.add_book.as_view(), name='add_book'),
    #path('edit/', views.edit_book.asview(), name='edit_book'),
    path('', views.default_page.as_view(), name='default_page'),
    path('remove/', views.delete_book.as_view(), name='delete_book'),
    path('<string:book_name>/chapter/add/', views.add_chapter.as_view(), name='add_chapter'),
]
