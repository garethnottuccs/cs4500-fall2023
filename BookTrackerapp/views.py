from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.views.generic import DeleteView
from .models import Book, Chapter, Character
from .forms import BookForm, ChapterForm, CharacterForm, ImageForm
from django.urls import reverse_lazy
from django.http import Http404
"""
BookTrackerapp Views
"""


# Create your views here.
class add_book(CreateView):
    """
    Adding each book
    """
    model = Book
    form_class = BookForm
    template_name = 'BookTrackerapp/book_add.html'
    success_url = reverse_lazy('book_list')


#class edit_book(UpdateView):
#   model = Book
#  template_name = 'BookTrackerapp/book_edit.html'


class default_page(ListView):
    """
    Home page of all added books
    """
    model = Book
    books = Book.objects.all()
    context = {'books': books}
    template_name = 'BookTrackerapp/home.html'
    #return render(CreateView, template_name, context)


class view_book(DetailView):
    """
    View each book individually
    """
    model = Book
    template_name = 'BookTrackerapp/view_book.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chapters'] = list(self.object.chapter_set.all())
        context['characters'] = list(self.object.character_set.all())
        return context


class edit_book(UpdateView):
    """
    Edit each book already added
    """
    model = Book
    fields = ["title", "summary", "page_number"]
    template_name = 'BookTrackerapp/book_edit.html'


class delete_book(DeleteView):
    """
    Delete book
    """
    model = Book
    template_name = 'BookTrackerapp/book_remove.html'
    success_url = reverse_lazy('book_list')


class add_chapter(CreateView):
    """
    Add chapters for each book
    """
    model = Chapter
    form_class = ChapterForm
    template_name = 'BookTrackerapp/chapter_add.html'


class add_character(CreateView):
    """
    Add characters for each book
    """
    model = Character
    form_class = CharacterForm
    template_name = 'BookTrackerapp/character_add.html'
    success_url = reverse_lazy('book_list')  # Change later


class edit_character(UpdateView):
    """
    Edit characters for each book
    """
    model = Character
    form_class = CharacterForm
    template_name = 'BookTrackerapp/character_edit.html'


class edit_chapter(UpdateView):
    """
    Edit chapters for each book
    """
    model = Chapter
    form_class = ChapterForm
    template_name = 'BookTrackerapp/chapter_edit.html'


# To be implemented
#class view_character(CreateView):
#  model = Character
#  template_name = 'BookTrackerapp/view_character.html'
#
#  def get_context_data(self, **kwargs):
#    context = super().get_context_data(**kwargs)
#    context['characters'] = list(self.object.character_set.all())
#    return context


def upload_image(request):
    """
    Upload book and character images
    """
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})
