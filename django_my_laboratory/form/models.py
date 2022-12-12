from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=30)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=30)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
