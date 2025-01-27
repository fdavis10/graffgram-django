from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

class Post(models.Model):

    LIVE = 'Жива'
    BUFF = 'Бафф'

    STATUS_OF_WORK = (
        (LIVE, 'Жива'),
        (BUFF, 'Бафф'),
    )

    # slug = models.SlugField()
    image = models.ImageField(upload_to='post/%Y/%m/%d', verbose_name='Изображение')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post', verbose_name='Автор')
    description = models.TextField(max_length=500, verbose_name='Описание')
    publish = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    status = MultiSelectField(choices=STATUS_OF_WORK, max_choices=2, blank=False, verbose_name='Статус работы')
    views = models.IntegerField(default = 0, verbose_name='Просмотры')
    likes = models.IntegerField(default = 0, verbose_name='Лайки')

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return reverse('blog:post_page', args=[int(self.pk)])

    def __str__(self):
        return str(self.pk)
    
    