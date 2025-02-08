from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.conf import settings
# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType

class Post(models.Model):

    LIVE = 'Жива'
    BUFF = 'Бафф'

    STATUS_OF_WORK = (
        (LIVE, 'Жива'),
        (BUFF, 'Бафф'),
    )

    # slug = models.SlugField()
    image = models.ImageField(upload_to='post/%Y/%m/%d', verbose_name='Изображение')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post', verbose_name='Автор')
    description = models.TextField(max_length=500, verbose_name='Описание')
    publish = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    status = models.CharField(max_length=10, choices=STATUS_OF_WORK, verbose_name='Статус работы', default=LIVE)
    views = models.IntegerField(default = 0, verbose_name='Просмотры')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', blank=True, verbose_name='Лайки')

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[int(self.pk)])

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return str(self.pk)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Комментарии')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, verbose_name='Автор')
    content = models.TextField(verbose_name='Комментарий')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.author} comment {self.post}'
    
class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_likes")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} liked {self.post.pk}"