# System imports
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# User imports
from .serializers import TaskCategorySerializer, UserProfileSerializer, UserSerializer, TaskSerializer
from .models import TaskCategory, UserProfile, Task


# Create your views here.


def home(request):
    return HttpResponse('<h1>API DOCS</h1>')


# FUNCTION BASED VIEWS

# @api_view(['GET', "POST"])
# def tasks(request):
#     if request.method == "POST":
#         return Response({"message": "this is a post reque"})
#     if request.method == "GET":
#         return Response({"message": "Hello Django"})


# CLASS BASED VIEWS


class TaskCategoryView(ListCreateAPIView):
    queryset = TaskCategory.objects.all()
    serializer_class = TaskCategorySerializer


class Users(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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


class UserProfile(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class Tasks(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
