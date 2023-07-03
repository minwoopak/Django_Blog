from django.db.models.signals import post_save
from django.contrib.auth.models import User # sender: the model that triggers the signal
from django.dispatch import receiver # receiver: the function that gets the signal and performs some task
from .models import Profile


@receiver(post_save, sender=User) # when a user is saved, send this signal (post_save)
def create_profile(sender, instance, created, **kwargs):
    if created: # if a User object is created
        Profile.objects.create(user=instance) # create a Profile object with the instance of the User that was created


@receiver(post_save, sender=User) # when a user is saved, send this signal (post_save)
def save_profile(sender, instance, **kwargs):
    instance.profile.save() # when the user is saved, save the profile as well