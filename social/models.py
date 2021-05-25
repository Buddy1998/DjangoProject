from django.db import models
from django.contrib.auth.models import User

class log(models.Model):
    name=models.CharField(max_length=100)
    text=models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, blank=True)

class Post(models.Model):
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User,  related_name='likes',default=0)
    dislikes = models.ManyToManyField(User, related_name='dislikes',default=0)



