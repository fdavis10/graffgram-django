from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_avatars/', blank=True, null=True)
    phone_number = models.CharField(max_length=100, unique=True, blank=False)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username
