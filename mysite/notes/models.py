from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    description = models.CharField(max_length=20)

    def __str__(self):
        return self.description

class Note(models.Model):
    title = models.CharField(max_length=15)
    body = models.TextField()
    locked = models.BooleanField(default=False)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='notes')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
