from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['author', 'pk']
    list_filter=['status', 'views', 'publish']
    readonly_fields=['views', ]
    
