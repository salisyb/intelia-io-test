from django.db import models


class Task(models.Model):
    text = models.CharField(max_length=255);
    day = models.CharField(max_length=255)
    reminder = models.BooleanField(default=False)