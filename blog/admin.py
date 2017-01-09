from django.contrib import admin
from .models import Post, Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]

admin.site.register(Post)
admin.site.register(Comment)
