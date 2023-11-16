from django import forms
from .models import Book, Chapter, Character, Image

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'summary']#, 'image']
      
# The previous ChapterForm, for reference
#class ChapterForm(forms.ModelForm):
#  class Meta:
#    model = Chapter
#    fields = ['book','title','chapternumber', 'description']
class ChapterForm(forms.ModelForm):
  class Meta:
      model = Chapter
      fields = ['book','title','chapternumber', 'description']

  #Need to overwrite the default init to fix dropdown menu
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['book'].queryset = Book.objects.all()
      self.fields['book'].widget = forms.Select(choices=[(book.pk, book.title) for book in Book.objects.all()])


class CharacterForm(forms.ModelForm):
  class Meta:
    model = Character
    fields = ['book', 'name', 'attributes', 'description']

  #Need to overwrite the default init to fix dropdown menu
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['book'].queryset = Book.objects.all()
    self.fields['book'].widget = forms.Select(choices=[(book.pk, book.title) for book in Book.objects.all()])

class ImageForm(forms.ModelForm):
  class Meta:
      model = Image
      fields = ['image']