from django.db import models
import datetime
from django.utils import timezone
from django.db.models import Count
from markdownx.models import MarkdownxField
from django.contrib.auth.models import User


# Create your models here.
#id는 자동생성
'''
class User(models.Model):
    nickname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    reg_date = models.DateTimeField('register_date',auto_now_add=True)
    lst_login = models.DateTimeField('latest login time', auto_now=True)

    def __str__(self):
        return self.nickname
'''

class CommonData(models.Model):
    created_date = models.DateTimeField('created_date',auto_now_add=True)
    changed_date = models.DateTimeField('changed_date', auto_now=True)

    class Meta:
        abstract = True


class Blog(CommonData):
    blogname = models.CharField(max_length=200)
    intro = models.CharField(max_length=1000)
    domain = models.CharField(max_length=20, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.blogname


class Category(CommonData):
    name = models.CharField(max_length=50)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    def __list__(blog_id):
        return Category.objects.filter(blog_id=blog_id).values('name','id',count=Count('post'))
#class Log(models.Model):


class Image(CommonData):
    image = models.ImageField()


class Post(CommonData):
    title = models.CharField(max_length=500)
    #content = models.TextField()
    content = MarkdownxField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)
    hit = models.IntegerField(default=0)
    published = models.BooleanField(default=False)

    def __str__(CommonData):
        return self.title
