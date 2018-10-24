from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# region Account Post Save

Account = get_user_model()


@receiver(post_save, sender=Account)
def assign_access_token_to_account(instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)

# endregion
