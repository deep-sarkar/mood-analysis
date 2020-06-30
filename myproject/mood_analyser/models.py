from django.db import models

class Message(models.Model):
    message = models.TextField(max_length=100, blank=True, null=True)
