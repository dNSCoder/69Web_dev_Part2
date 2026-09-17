from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=250)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [ "done", "-created_at"]

    def __str__(self):
        return self.title