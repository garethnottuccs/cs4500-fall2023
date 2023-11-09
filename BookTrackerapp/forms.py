from django import forms
from .models import Book, Chapter

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'summary']

class ChapterForm(forms.ModelForm):
  class Meta:
    model = Chapter
    fields = ['book','title','chapternumber', 'description']