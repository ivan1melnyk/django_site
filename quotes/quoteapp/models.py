from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=80)
    born_date = models.DateField()
    born_place = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name


class Quote(models.Model):
    quote = models.TextField()
    authors = models.ManyToManyField(Author, related_name='quotes')
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.quote[:50]