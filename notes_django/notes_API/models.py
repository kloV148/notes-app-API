from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    created_by = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, null=False, blank=True)
    content = models.TextField(max_length=1024, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)
