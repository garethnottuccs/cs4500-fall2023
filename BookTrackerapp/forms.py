from django import forms
from .models import Book, Chapter, Character, Image


class BookForm(forms.ModelForm):
    """
    Form to handle Book model data
    """
    class Meta:
        model = Book
        fields = ['title', 'summary', 'image', 'page_number', 'start_date', 'end_date']


# The previous ChapterForm, for reference
#class ChapterForm(forms.ModelForm):
#  class Meta:
#    model = Chapter
#    fields = ['book','title','chapternumber', 'description']
class ChapterForm(forms.ModelForm):
    """
    Form to handle Chapter model data
    """
    class Meta:
        model = Chapter
        fields = ['book', 'title', 'chapternumber', 'description']

    #Need to overwrite the default init to fix dropdown menu
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['book'].queryset = Book.objects.all()
        self.fields['book'].widget = forms.Select(
            choices=[(book.pk, book.title) for book in Book.objects.all()])


class CharacterForm(forms.ModelForm):
    """
    Form to handle Character model data
    """
    class Meta:
        model = Character
        fields = ['book', 'name', 'attributes', 'description', 'image']


#Need to overwrite the default init to fix dropdown menu

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['book'].queryset = Book.objects.all()
        self.fields['book'].widget = forms.Select(
            choices=[(book.pk, book.title) for book in Book.objects.all()])


class ImageForm(forms.ModelForm):
    """
    Form to handle Image model data
    """
    class Meta:
        model = Image
        fields = ['image']
