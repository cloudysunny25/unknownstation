from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
#id는 자동생성
class User(models.Model):
    nickname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    reg_date = models.DateTimeField('register_date',auto_now_add=True)
    lst_login = models.DateTimeField('latest login time', auto_now=True)

    def __str__(self):
        return self.nickname





class Blog(models.Model):
    blogname = models.CharField(max_length=200)
    comment = models.CharField(max_length=1000)
    reg_date = models.DateTimeField('register_date',auto_now_add=True)
    chng_date = models.DateTimeField('changed_date', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.blogname


class Category(models.Model):
    name = models.CharField(max_length=50)
    reg_date = models.DateTimeField('register_date', auto_now_add=True)
    chng_date = models.DateTimeField('changed_date', auto_now=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
#class Log(models.Model):



class Post(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    reg_date = models.DateTimeField('register_date', auto_now_add=True)
    chng_date = models.DateTimeField('changed_date', auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
