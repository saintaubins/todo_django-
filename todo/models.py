from django.db import models

from datetime import datetime

class Todos(models.Model):
    text = models.CharField(max_length=100, default='default')
    when = models.CharField(max_length=500, default='default')
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.text

