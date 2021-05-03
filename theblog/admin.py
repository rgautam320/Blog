from django.contrib import admin
from .models import Post, Profile, Comment, Category

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)
