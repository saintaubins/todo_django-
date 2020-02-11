from django.db import models

class Todos(models.Model):
    author = models.CharField(max_length=200)
    nationality = models.CharField(max_length=100)
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.author + " , " + self.nationality + " , " + self.title

