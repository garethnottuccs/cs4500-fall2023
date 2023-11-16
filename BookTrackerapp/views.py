from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.views.generic import DeleteView
from .models import Book, Chapter, Character
from .forms import BookForm, ChapterForm, CharacterForm, ImageForm
from django.urls import reverse_lazy


# Create your views here.
class add_book(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'BookTrackerapp/book_add.html'
    success_url = reverse_lazy('book_list')


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
    template_name = 'BookTrackerapp/book_edit.html'


class delete_book(DeleteView):
    model = Book
    template_name = 'BookTrackerapp/book_remove.html'
    success_url = reverse_lazy('book_list')


class add_chapter(CreateView):
    model = Chapter
    form_class = ChapterForm
    template_name = 'BookTrackerapp/chapter_add.html'


class add_character(CreateView):
    model = Character
    form_class = CharacterForm
    template_name = 'BookTrackerapp/character_add.html'
    success_url = reverse_lazy('book_list') # Change later


class edit_character(UpdateView):
    model = Character
    form_class = CharacterForm
    template_name = 'BookTrackerapp/character_edit.html'


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
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})
