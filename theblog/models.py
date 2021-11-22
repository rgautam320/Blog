from django.db import models
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)

    short_desc = models.CharField(max_length=255)

    header_image = models.ImageField(null=True, upload_to="blogs")

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    category = models.CharField(max_length=255)

    body = RichTextField(blank=True, null=True)

    post_date = models.DateTimeField(auto_now_add=True)

    likes = models.ManyToManyField(User, related_name='blog_post')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + " | " + str(self.author.first_name)

    def get_absolute_url(self):
        # return reverse('article_detail', args=(str(self.id)))
        return reverse('home')


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255)
    job_title = models.CharField(null=True, blank=True, max_length=255)
    phone = models.CharField(null=True, blank=True, max_length=10)
    # profile_picture = models.CharField(max_length=255, default="")
    profile_picture = models.ImageField(null=True, upload_to="profiles")
    website_URL = models.CharField(null=True, blank=True, max_length=255)
    facebook_URL = models.CharField(null=True, blank=True, max_length=255)
    twitter_URL = models.CharField(null=True, blank=True, max_length=255)
    instagram_URL = models.CharField(null=True, blank=True, max_length=255)
    youtube_URL = models.CharField(null=True, blank=True, max_length=255)
    github_URL = models.CharField(null=True, blank=True, max_length=255)
    linkedin_URL = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             related_name='comments',
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title
