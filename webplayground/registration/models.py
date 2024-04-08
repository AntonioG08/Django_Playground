from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename


# Create your models here.
class Profile(models.Model):
    # With this we stablish a relation 1 to 1, indicating that there can only exist ONE user to ONE profile, no more
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['user__username']


# This function is a signal that we will use to ensure that every user created has a profile
@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    # We need to make sure that the signal is triggered only when the user has been created for first time using the IF
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        # print('Se acaba de crear un usuario y su perfil enlazado')
