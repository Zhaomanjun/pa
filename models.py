from django.db import models
from django.utils import timezone
# Create your models here.

class Author(models.model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def _unicode_(self):
        return self.name

class Blog(models.Model):
    title = models.Charfield(max_length=50)
    content = models.TextField()
    counter = models.IntegerField(default=0)
    pubDate = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author)

    def _unicode_(self):
        return self.title