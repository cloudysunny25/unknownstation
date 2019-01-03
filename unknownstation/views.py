from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User,Blog,Post,Category
from django.views import generic
from django.template import loader
from django.urls import reverse
from django.contrib.sessions.backends.db import SessionStore
from django.core import serializers
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .forms import LoginForm
# Create your views here.


def is_blog_owner(self):
    blog = Blog.objects.get(id=2)
    return self.request.user.username==blog.user.username


def index(request):
    #get()은 하나의 결과값만 가져옴. 여러건을 가져올 땐 filter
    #base data
    blog = Blog.objects.get(blogname='eggclothes')
    user = blog.user
    categories = Category.__list__(blog_id=2)
    request.session['blog_info'] = {'id':blog.id, 'blogname':blog.blogname, 'user':{'username':user.username} }
    request.session['category_info'] = list(categories)
    request.session['user_info'] = {'nickname':user.username, 'id':user.id}

    #index data
    paginator = Paginator(Post.objects.order_by('-created_date'), 5)
    post_list = paginator.get_page(1)
    context = {
        'post_list' : post_list
    }
    template = loader.get_template('unknownstation/index.html')
    return HttpResponse(template.render(context, request))

def postlist(request,page):
    #index data
    paginator = Paginator(Post.objects.order_by('-created_date'), 5)
    if page is None:
        page = 1

    post_list = paginator.get_page(page)
    context = {
        'post_list' : post_list
    }
    template = loader.get_template('unknownstation/index.html')
    return HttpResponse(template.render(context, request))


def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    template = loader.get_template('unknownstation/detail.html')
    context = {
     'post_info':post,
    }
    return HttpResponse(template.render(context, request))

@login_required
def write(request):

    template = loader.get_template('unknownstation/write.html')
    user_info = User.objects.get(username='eggkim')
    blog_info = Blog.objects.get(id=2)

    #form = PostForm()
    return render(request, 'unknownstation/write.html',{'blog_info':blog_info, 'user_info':user_info})

@login_required
def updateView(request,post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'unknownstation/update.html',{'post_info':post, })

@login_required
def update(request):
    post = Post.objects.get(id=request.POST['post_id'])
    post.title = request.POST['title']
    post.content = request.POST['content']
    post.content_markdown = request.POST['content_markdown']
    post.category = Category.objects.get(id=request.POST['category'])
    if request.POST['published']=='publish':
        post.published=True
    else:
        post.published=False
    post.save()
    print(request.POST['content_markdown']+"???")
    categories = Category.__list__(request.session['blog_info']['id'])
    request.session['category_info'] = list(categories)
    return HttpResponseRedirect(reverse('unknownstation:index'))

@login_required
def delete(request):
    post = Post.objects.get(id=request.POST['post_id'])
    post.delete()
    return HttpResponseRedirect(reverse('unknownstation:index'))


@login_required
def register(request):
    category = Category.objects.get(pk=request.POST['category'])
    user = User.objects.get(id=request.session.get('user_info')['id'])
    blog = Blog.objects.get(id=request.session.get('blog_info')['id'])
    post = Post(title=request.POST['title'], content=request.POST['content'], content_markdown = request.POST['content_markdown'], category=category, user=user, blog=blog)
    if request.POST['published']=='publish':
        post.published=True
    else:
        post.published=False
    post.save()
    categories = Category.__list__(request.session['blog_info']['id'])
    request.session['category_info'] = list(categories)
    return HttpResponseRedirect(reverse('unknownstation:index'))


def __login__(request):
    #form = LoginForm()
    return render(request, 'unknownstation/login.html')

def __logout__(request):
    logout(request)
    return HttpResponseRedirect(reverse('unknownstation:index'))


def auth(request):
    nickname = request.POST.get('nickname')
    password = request.POST.get('password')
    user = authenticate(request, username=nickname, password=password)
    if user is not None:
        login(request,user)
        return HttpResponseRedirect(reverse('unknownstation:index'))
    else:
        return HttpResponse("nickname and password are didn't match")



def byCategory(request, category, page):
    category_info = None
    for c in request.session.get('category_info'):
        if c['name']==category:
            category_info = c
    post_list = Post.objects.filter(category_id=category_info['id']).order_by('-created_date')
    paginator = Paginator(post_list, 5)
    post_list = paginator.get_page(page)
    return render(request, 'unknownstation/listByCategory.html', {'post_list':post_list, 'category_info':category_info})

def byKeyword(request):
    keyword = request.GET['keyword']
    page = request.GET['page']
    post_list = Post.objects.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword)).order_by('-created_date')
    paginator = Paginator(post_list, 5)
    page = paginator.get_page(page)
    return render(request, 'unknownstation/listByKeyword.html',{'post_list':page, 'keyword':keyword})

def category(request):
    categories = Category.__list__(blog_id=2)
    return render(request,'unknownstation/category.html',{'categories':categories})

def month(request):
    dates = Post.objects.dates('created_date','month')
    month_list = list()
    year_list = list()
    for date in dates:
        year_list.append(date.year)
        mrow = {'year':date.year,'month':date.month,'count':Post.objects.filter(created_date__year=date.year,created_date__month=date.month).count()}
        month_list.append(mrow)
    return render(request, 'unknownstation/month.html',{'year_list':year_list,'month_list':month_list})

def byMonth(request, year, month, page):
    post_list = Post.objects.filter(created_date__year=year,created_date__month=month).order_by('-created_date')
    paginator = Paginator(post_list, 5)
    page = paginator.get_page(page)
    mrow = {'year':year,'month':month,'count':Post.objects.filter(created_date__year=year,created_date__month=month).count()}
    return render(request,'unknownstation/listByMonth.html',{'post_list':page, 'month_info':mrow})
