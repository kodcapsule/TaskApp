from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Task, TaskCategory, UserProfile, SubTask


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'due_date',
                  'priority', 'status', 'created_at', 'updated_at']


class TaskCategorySerializer(ModelSerializer):
    class Meta:
        model = TaskCategory
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "date_joined"]


class UserProfileSerializer (ModelSerializer):

    class Meta:
        model = UserProfile
        fields = "__all__"


class SubTaskSerializer (ModelSerializer):
    class Meta:
        model = SubTask
        # fields: ['id', 'task','title','description','due_date','completed','status','created_at','updated_at']
        fields = '__all__'
