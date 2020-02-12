from django.db import models
from datetime import datetime

class Todos(models.Model):
    proj_desc = models.CharField(max_length=100, default='Project Description')
    when = models.CharField(max_length=500, default='Time of Day')
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.text

class Lists(models.Model):
    todos = models.ForeignKey(Todos, on_delete=models.CASCADE, related_name='lists')
    name = models.CharField(max_length=100, default='Add your name')
    comment = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.todos.name 

