from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class FriendShip(models.Model):

    STATUS_FRIEND = (
        ('pending', 'Ожидание'),
        ('accepted', 'Одобрено'),
        ('declined', 'Отклонено'),
    )

    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='friendship_created', on_delete=models.CASCADE)
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='friendship_received', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_FRIEND, default='pending')

    class Meta:
        unique_together = ('from_user', 'to_user')

    def __str__(self):
        return f'{self.from_user.username} >> {self.to_user.username} : {self.status}!'
    