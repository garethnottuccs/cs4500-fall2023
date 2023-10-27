from django.db import models
from django.urls import reverse

class Book(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=100)
  #image = models.ImageField(upload_to='images/')

  def get_absolute_url(self):
    return reverse("book_list")