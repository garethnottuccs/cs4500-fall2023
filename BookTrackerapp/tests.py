##To run coverage
#/home/runner/group1-fall2023/venv/bin/python3 -m coverage run --#source='.' manage.py test BookTracker

##To get the coverage report
#/home/runner/group1-fall2023/venv/bin/python -m coverage report

from django.test import TestCase
from django.urls import reverse
from .models import Book, Chapter  #, Character, Image
#For asgi.py tests
from django.core.asgi import get_asgi_application
from BookTracker import asgi
#OMMITEED WSGI FROM TESTING DUE TO COMPLEXITY
#For form.py tests
from .forms import BookForm, ChapterForm, CharacterForm, ImageForm
from datetime import date

# Create your tests here.


# Define a test class for testing the Book model
##################################BOOK TEST################################
class BookTest(TestCase):
    def setUp(self):
        # Create a new Book object for testing with a title and summary
        self.book = Book.objects.create(title='Test Book',
                                        summary='Test Summary',
                                        page_number=0,
                                        start_date=date.today(),
                                        end_date=date.today(),)

    def test_delete_book(self):
        # Simulates a POST request to delete a book
        response = self.client.post(
            reverse('delete_book', kwargs={'pk': self.book.pk}))
        # Check if the response status code is 302 (indicating a successful redirect)
        self.assertEqual(response.status_code, 302)
        # Check if the book with the given primary key no longer exists in the database
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())


##################################CHAPTER TEST################################
class ChapterTest(TestCase):
    def setUp(self):
        # Create a new Book object for testing with a title and summary
        self.book = Book.objects.create(title='Test Book',
                                        summary='Test Summary',
                                        page_number=0)
        # Create a new Chapter object for testing with a title, description, and associated book
        self.book.chapter = Chapter.objects.create(
            book=self.book,
            title='Test Chapter',
            #There is a check to ensure a valid chapter number, need this line
            chapternumber=1,
            description='Test Summary')

    def test_view_book(self):
        # Simulates a GET request to view a book
        response = self.client.get(
            reverse('view_book', kwargs={'pk': self.book.pk}))
        # Check if the response status code is 200 (indicating a successful request)
        self.assertEqual(response.status_code, 200)
        # Check if the response contains the expected HTML elements
        self.assertContains(response, '<h1>Test Book</h1>')
        self.assertContains(response, 'Test Chapter')
        self.assertContains(response, 'Test Summary')
        self.assertContains(response, 0)


##################################ASGI TEST################################
class AsgiTests(TestCase):
    def test_asgi_application(self):
        """
      Test that the ASGI application is correctly configured.
      """
        try:
            # Attempt to get the ASGI application
            # Use the result to avoid "unused variable" warning
            _ = get_asgi_application()
        except Exception as e:
            # Fail the test if an exception is raised
            self.fail(f"Failed to get ASGI application: {str(e)}")

    def test_import_asgi_module(self):
        """
      Test that the asgi.py module can be imported without errors.
      """
        try:
            # Use the imported module to avoid "unused variable" warning
            _ = asgi
        except ImportError as e:
            self.fail(f"Failed to import asgi.py module: {str(e)}")


##################################URLS TEST################################
class UrlsTests(TestCase):
    def test_reverse_urls(self):
        """
      Test that all defined URLs can be reversed without errors.
      """
        try:
            _ = reverse('book_list')
        except Exception as e:
            self.fail(f"Failed to reverse URLs: {str(e)}")


##################################FORM TEST################################
class FormsTest(TestCase):
    def test_book_form_valid(self):
        # Create a valid form data dictionary
        form_data = {
            'title': 'Test Title',
            'summary': 'Test Summary',
            'page_number': 0,
            'start_date': date.today(),
            'end_date': date.today(),
            'image': 'BookTrackerapp/static/images/default.jpeg',
        }

        # Create a form instance with the provided data
        form = BookForm(data=form_data)

        # Check if the form is valid
        self.assertTrue(form.is_valid())

    def test_chapter_form_valid(self):
        # Create a valid form data dictionary
        form_data = {
            'title': 'Test Title',
            'chapternumber': 1,
            'description': 'Test Description',
        }

        # Create a form instance with the provided data
        form = ChapterForm(data=form_data)

        # Check if the form is not valid
        self.assertFalse(form.is_valid())

    def test_character_form_valid(self):
        # Create a valid form data dictionary
        form_data = {
            'name': 'Test Character',
            'attributes': 'Test Attributes',
            'description': 'Test Description',
        }

        # Create a form instance with the provided data
        form = CharacterForm(data=form_data)

        # Check if the form is not valid
        self.assertFalse(form.is_valid())

    def test_image_form_valid(self):
        # Create a valid form data dictionary
        form_data = {
            'image': 'BookTrackerapp/static/images/default.jpeg',
        }

        # Create a form instance with the provided data
        form = ImageForm(data=form_data)

        # Check if the form is not valid
        self.assertFalse(form.is_valid())
