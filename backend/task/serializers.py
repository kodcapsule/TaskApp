from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task, TaskCategory, UserProfile, SubTask


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'due_date',
                  'priority', 'status', 'created_at', 'updated_at']


class TaskCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskCategory
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "date_joined"]


class UserProfileSerializer (serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = "__all__"


class SubTaskSerializer (serializers.ModelSerializer):
    class Meta:
        model = SubTask
        # fields: ['id', 'task','title','description','due_date','completed','status','created_at','updated_at']
        fields = '__all__'


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})
