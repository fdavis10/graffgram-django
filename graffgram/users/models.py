from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField


class User(AbstractUser):

    VERIFICATED = 'Верифицированн'
    STANDART = 'Стандартный'

    image = models.ImageField(upload_to='users_avatars/', blank=True, null=True, default='users_avatars/default_avatar.jpg')
    phone_number = models.CharField(max_length=100, unique=True, blank=False)
    is_verified = models.BooleanField(default=False, verbose_name="Статус пользователя")
    bio = models.TextField(blank=True, null=True, verbose_name='Описание')

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username
