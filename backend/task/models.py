from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import uuid


# Create your models here.


class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job = models.CharField(max_length=500, default='Software Engineer')
    # profileImage = models.ImageField(upload_to= 'images/', default='profile_image.jpg')
    # phone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user.username}'


class Task(models.Model):
    PRIORITY = [('high', 'High'), ('medium', 'Medium'), ('low', 'Low')]
    STATUS = [('incomplete', 'Incomplete'), ('complete', 'Complete')]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    taskCategory = models.OneToOneField(
        'TaskCategory', on_delete=models.CASCADE)
    title = models.CharField(max_length=800, default='General Tasks')
    description = models.TextField(default='')
    due_date = models.DurationField()
    priority = models.CharField(max_length=100, choices=PRIORITY)
    status = models.CharField(max_length=100, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TaskCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=600)
    color = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class SubTask (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    due_date = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
