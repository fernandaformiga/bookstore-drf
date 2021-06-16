from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    STOCK = (
        ('A', 'available'),
        ('U', 'unavailable'),
        ('F', 'few units left')
    )
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    year = models.IntegerField()
    genre = models.CharField(max_length=50)
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.name