from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.views.generic import DeleteView
from .models import Book, Chapter
from .forms import BookForm, ChapterForm
from django.urls import reverse_lazy


# Create your views here.
class add_book(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'BookTrackerapp/book_add.html'


#class edit_book(UpdateView):
#   model = Book
#  template_name = 'BookTrackerapp/book_edit.html'


class default_page(ListView):
    model = Book
    books = Book.objects.all()
    context = {'books': books}
    template_name = 'BookTrackerapp/home.html'
    #return render(CreateView, template_name, context)

class view_book(DetailView):
  model = Book
  template_name = 'BookTrackerapp/view_book.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['chapters'] = list(self.object.chapter_set.all())
    return context
  

class edit_book(UpdateView):
    model = Book
    fields = ["title", "summary"]


class delete_book(DeleteView):
    model = Book
    template_name = 'BookTrackerapp/book_remove.html'
    success_url = reverse_lazy('book_list')


class add_chapter(CreateView):
    model = Chapter
    form_class = ChapterForm
    template_name = 'BookTrackerapp/chapter_add.html'
