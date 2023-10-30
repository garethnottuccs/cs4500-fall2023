from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic import DeleteView
from .models import Book


# Create your views here.
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Book


# Create your views here.
class add_book(CreateView):
    model = Book
    template_name = 'BookTrackerapp/book_add.html'

class default_page(ListView):
    model = Book
    books = Book.objects.all()
    context = {'books': books}
    template_name = 'BookTrackerapp/home.html'
    #return render(CreateView, template_name, context)

class delete_book(DeleteView):
  model = Book
  template_name = 'BookTrackerapp/delete_book.html'
