from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Author(models.Model):
    author = models.CharField(max_length=10000)



    def __str__(self):
        return self.author

class Book(models.Model):
    title = models.CharField(max_length=10000)
    author = models.ManyToManyField(Author, related_name='book_author')
    description = models.CharField(max_length=10000)
    checked_out = models.DateTimeField(null=True)
    check_in = models.BooleanField(default=False)
    checked_out_by = models.CharField(default='', max_length=10000)

    def __str__(self):
        return self.title

