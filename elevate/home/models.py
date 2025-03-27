from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
    
class Review(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=200)
    review_title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.reviewer_name}"