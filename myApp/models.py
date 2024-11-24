import os
from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    id_user = models.IntegerField(primary_key=True, default=0)
    bio = models.TextField(blank=True , default='')
    profileimg = models.ImageField(upload_to='profile_images', default='Images/doll.jpg')
    
    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='post_images')
    audio = models.FileField(upload_to='audio_files' , blank=True, null=True)
    
    # #testing
    # video = models.FileField(upload_to='audio_files' , blank=True, null=True)
    # #testing
    
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user
    
class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
#-------------------------commenting

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.text}'


class YourModel(models.Model):
    file = models.FileField(upload_to='audio_files')

    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        if extension in ['mp3', 'wav' , ...]:
            return 'audioo'
        if extension in ['mp4', 'mpg', 'mpeg', ...]:
            return 'videoo'