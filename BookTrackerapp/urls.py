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
from django.urls import path  #, include
from BookTrackerapp import views
from .views import upload_image
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.default_page.as_view(), name='book_list'),
    path('add/', views.add_book.as_view(), name='add_book'),
    path('<int:pk>/view/', views.view_book.as_view(), name='view_book'),
    path('<int:pk>/edit/', views.edit_book.as_view(), name='edit_book'),
    path('<int:pk>/remove/', views.delete_book.as_view(), name='delete_book'),
    path('<int:pk>/chapter/add/',
         views.add_chapter.as_view(),
         name='add_chapter'),

    #path('<int:pk>/chapter/', views.view_chapter.as_view(), name='chapter'),
    path('<int:pk>/character/add/',
         views.add_character.as_view(),
         name='add_character'),
    path('<int:pk>/character/edit/',
         views.edit_character.as_view(),
         name='edit_character'),
    path('<int:pk>/chapter/edit/',
         views.edit_chapter.as_view(),
         name='edit_chapter'),
    path('upload/', upload_image, name='upload_image'),

    # To be inserted: path('<int:pk>/character/',
    # views.view_character.as_view(), name="character"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
