from django.db import models

# Create your models here.


class Todo(models.Model):
    """A simple todo entry"""

    is_done = models.BooleanField()
    name = models.CharField(max_length=128)
