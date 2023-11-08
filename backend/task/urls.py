from django.urls import path

from .views import home,  TaskCategoryView, Users, UserProfile, Tasks

urlpatterns = [
    path('', home, name="index"),

    path('category', TaskCategoryView.as_view(), name='category'),
    path('users', Users.as_view(), name='users'),
    path('profiles', UserProfile.as_view(), name='user_profiles'),
    path('tasks', Tasks.as_view(), name='user_profiles')
]
