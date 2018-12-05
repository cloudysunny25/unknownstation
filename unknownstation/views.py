from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User,Blog,Post,Category
from django.views import generic
from django.template import loader
from .forms import PostForm,LoginForm
from django.urls import reverse
from django.contrib.sessions.backends.db import SessionStore
from django.core import serializers
import json
# Create your views here.
def index(request):
    latest_post = Post.objects.order_by('-reg_date')[:1]
    latest_post_list = Post.objects.order_by('-reg_date')[:5]
    user_info = User.objects.get(nickname='norang')
    blog_info = Blog.objects.get(id=6)
    category_info = Category.objects.all()
    category_list = [c.name for c in category_info]
    template = loader.get_template('unknownstation/index.html')
    request.session['blogname'] = blog_info.blogname
    request.session['category_info'] = category_list
    context = {
        'post_info': latest_post,
        #'category_info': category_info,
        'latest_post_list' : latest_post_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, post_id):

    post = Post.objects.get(id=post_id)
    template = loader.get_template('unknownstation/detail.html')
    context = {
     'post_info':post,
    }
    return HttpResponse(template.render(context, request))

def write(request):
    '''
    template = loader.get_template('unknownstation/write.html')
    user_info = User.objects.get(nickname='norang')
    blog_info = Blog.objects.get(id=6)
    context = {
            'blog_info' : blog_info,
            'user_info' : user_info,
    }
    '''
    #form = PostForm()
    category = Category.objects.all()
    return render(request, 'unknownstation/write.html',{'category_info':category})

def updateView(request,post_id):
    post = Post.objects.get(id=post_id)
    category = Category.objects.all()
    return render(request, 'unknownstation/update.html',{'post_info':post, 'category_info':category})

def update(request):
    post = Post.objects.get(id=request.POST['post_id'])
    post.title = request.POST['title']
    post.content = request.POST['content']
    post.category = Category.objects.get(id=request.POST['category'])
    post.save()
    return HttpResponseRedirect(reverse('unknownstation:index'))

def delete(request):
    post = Post.objects.get(id=request.POST['post_id'])
    post.delete()
    return HttpResponseRedirect(reverse('unknownstation:index'))



def register(request):
    category = Category.objects.get(pk=request.POST['category'])
    user = User.objects.get(pk=1)
    post = Post(title=request.POST['title'], content=request.POST['content'], category=category, user=user)
    post.save()
    return HttpResponseRedirect(reverse('unknownstation:index'))

def login(request):
    form = LoginForm()
    return render(request, 'unknownstation/login.html', {'form':form})

def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('unknownstation:index'))

def auth(request):
    nickname = request.POST['nickname']
    password = request.POST['password']
    try:
        user = User.objects.get(nickname=nickname)
        if user.password==password:
            request.session['nickname'] = user.nickname
            request.session['user_id'] = user.id
            return HttpResponseRedirect(reverse('unknownstation:index'))
        else:
            return HttpResponse("nickname and password are didn't match")
    except:
        return HttpResponse("nickname "+nickname+" is not exist")
