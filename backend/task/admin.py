from django.contrib import admin

from . models import TaskCategory, UserProfile, Task

# Register your models here.
admin.site.register(TaskCategory)
admin.site.register(UserProfile)
admin.site.register(Task)
