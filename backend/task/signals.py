from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .models import UserProfile


# Create signals to handle the creation and updating of user profile
@receiver(post_save, sender=User)
def createUserProfile(sender, instance, created, *args, **kwargs):
    if created:
        user_profile = UserProfile.objects.create(user=instance)
        token = Token.objects.create(user=instance)
        print(f'==============={user_profile}================')
        print(f'User profile for {user_profile} created')
        print(f'token {token} generated')
        print(f'===========================================')
    else:
        # user_profile = instance.save()
        print('=============== User  Updated================')
        print(f'User {kwargs}, {args}profile updated')


# @receiver(post_save, sender=User)
# def updateUserProfile(sender, instance, created, **kwargs):
#     if created == False:
#         # user_profile = instance.save()
#         print('=============== User Profile ================')
#         print(f'User {kwargs}profile updated')
