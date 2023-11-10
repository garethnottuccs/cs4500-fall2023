from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(max_length=500)

    #image = models.ImageField(upload_to='images/')

    def get_absolute_url(self):
        return reverse("book_list")


class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    chapternumber = models.IntegerField(default=0)
    description = models.TextField(max_length=1000)

    def get_absolute_url(self):
        return reverse("book_list")


class Character(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    attributes = models.CharField(max_length=500)
    description = models.TextField(max_length=1000)
    #image = models.ImageField(upload_to='images/')
