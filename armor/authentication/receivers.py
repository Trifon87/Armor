# from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from armor.authentication.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, *args, **kwargs):
    if created:
        profile = Profile(user=instance, display_name=instance.username, profile_picture=instance.profile_picture)
        profile.save()

from receivers import *