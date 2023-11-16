from django.test import TestCase
from django.urls import reverse
from models import Book, Chapter
# Create your tests here.

# Define a test class for testing the Book model
class BookTest(TestCase):
    def setUp(self):
        # Create a new Book object for testing with a title and summary
        self.book = Book.objects.create(title='Test Book', summary='Test Summary')

    def test_delete_book(self):
        # Simulates a POST request to delete a book
        response = self.client.post(reverse('delete_book', kwargs={'pk': self.book.pk}))
        # Check if the response status code is 302 (indicating a successful redirect)
        self.assertEqual(response.status_code, 302)
        # Check if the book with the given primary key no longer exists in the database
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())

class ChapterTest(TestCase):
  def setUp(self):
    self.book = Book.objects.create(title='Test Book', summary='Test Summary')
    self.book.chapter = Chapter.objects.create(book = self.book, title='Test Chapter', description='Test Summary')
    
  def test_view_book(self):
    response = self.client.get(reverse('view_book', kwargs={'pk': self.book.pk}))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, '<h1>Test Book</h1>')
    self.assertContains(response, 'Test Chapter')
    self.assertContains(response, 'Test Summary')
    