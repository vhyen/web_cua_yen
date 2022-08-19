from django.contrib import admin
from .models import Post
# yen - 123456

# Interface for Post
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['title']

# Register your models here.
admin.site.register(Post, PostAdmin)

