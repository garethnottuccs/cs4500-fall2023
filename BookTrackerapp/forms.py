from django import forms
from .models import Book, Chapter, Character

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'summary']

class ChapterForm(forms.ModelForm):
  class Meta:
    model = Chapter
    fields = ['book','title','chapternumber', 'description']

class CharacterForm(forms.ModelForm):
  class Meta:
    model = Character
    fields = ['book', 'name', 'attributes', 'description']