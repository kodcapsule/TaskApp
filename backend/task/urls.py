from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import RedirectView


from .views import home,  TaskCategoryView, Users, UserProfile, Tasks, UserLogin, UpdateReadDeleteUser,  ReadUpdateTask, DeleteTask, UserLogout


urlpatterns = [
    path('', home, name="index"),
    path('category', TaskCategoryView.as_view(), name='category'),
    path('users', Users.as_view(), name='users'),
    path('profiles', UserProfile.as_view(), name='user_profiles'),
    path('tasks', Tasks.as_view(), name='user_profiles'),
    path('task/<str:pk>/', ReadUpdateTask.as_view(), name='retrieve-update-task'),
    path('deleteTask/<str:pk>/', DeleteTask.as_view(), name='delete-task'),
    path('login', UserLogin.as_view(), name='user_login'),
    path('logout', UserLogout.as_view(), name='user_logout')

]
