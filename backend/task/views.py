# System imports
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.shortcuts import redirect


# User imports
from .serializers import TaskCategorySerializer, UserProfileSerializer, UserSerializer, TaskSerializer, UserLoginSerializer
from .models import TaskCategory, UserProfile, Task


# FUNCTION BASED VIEWS

def home(request):
    return HttpResponse('<h1>API DOCS</h1>')


# CLASS BASED VIEWS
class TaskCategoryView(ListCreateAPIView):
    queryset = TaskCategory.objects.all()
    serializer_class = TaskCategorySerializer

# class-based views for performing actions on the Users model


class Users(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        data = {}
        if serializer.is_valid():
            newUser = serializer.save()
            token = Token.objects.get(user=newUser).key
            data['email'] = newUser.email
            data['username'] = newUser.username
            data['token'] = token
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateReadDeleteUser(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserProfile(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAdminUser]


# class-based views for performing actions on the task model
# Only admin users can read create , update and delete task.
# An authenticated user can read and update task
class Tasks(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        data = {}
        if serializer.is_valid():
            newTask = serializer.save()
            data['title'] = newTask.title
            data['description'] = newTask.description
            data['priority'] = newTask.priority
            data['status'] = newTask.status
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReadUpdateTask (RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class DeleteTask(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAdminUser]


#  Users login view
class UserLogin(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                # return Response({'token': token.key}, status=status.HTTP_200_OK)
                return Response({'message': 'Login successful. Redirecting...'}, status=status.HTTP_200_OK, headers={'Location': '/login-success/'})

            else:
                return Response({'error': 'Invalid credentials, check your username and password'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
