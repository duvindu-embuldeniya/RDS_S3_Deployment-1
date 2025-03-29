from django.db import models
from django.contrib.auth.models import User

class Thought(models.Model):
    author = models.ForeignKey(User, on_delete=models.ForeignKey)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} | {self.author.username}"