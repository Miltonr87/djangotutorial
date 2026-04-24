from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=70, null=True, blank=True)
    last_name = models.CharField(max_length=70, null=True, blank=True)
    title = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE,
        related_name='books'
    )
    isbn = models.CharField(max_length=13, unique=True)
    publication_date = models.DateField()
    pages = models.IntegerField()
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.title} by {self.author}"