from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
"""
This is the models for the BookTracking 
"""


class Book(models.Model):
    """
    Model to represent a book
     """
    title = models.CharField(max_length=100)
    summary = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    page_number = models.IntegerField(default=0)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def get_absolute_url(self):
        """
        Method to get the absolute URL for a book
        """
        return reverse("book_list")


class Chapter(models.Model):
    """
    Model to represent a chapter
    """
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    #Ensures there aren't negative chapters.
    chapternumber = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.TextField(max_length=1000)

    def get_absolute_url(self):
        """
        Method to get the absolute URL for a chapter
        """
        return reverse("book_list")


class Character(models.Model):
    """
    Model to represent a character
    """
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    attributes = models.CharField(max_length=500)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def get_absolute_url(self):
        """
      Method to get the absolute URL for a chapter
      """
        return reverse("book_list")


class Image(models.Model):
    """
    Model to represent an image
    """
    image = models.ImageField(upload_to='images/')
