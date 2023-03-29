from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Task(models.Model):
    task = models.CharFiled(max_length=50)
    description = models.TextFiled()
    complited = models.BoolenaField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    
