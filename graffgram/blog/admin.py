from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['author', 'pk']
    list_filter=['status', 'views', 'publish']
    readonly_fields=['views', ]
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'content', 'created', ]
    readonly_fields = ['post', 'author', 'content', 'created', ]