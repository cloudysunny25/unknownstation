from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User,Blog,Post,Category
from django.views import generic
from django.template import loader
from .forms import PostForm,LoginForm
from django.urls import reverse
from django.contrib.sessions.backends.db import SessionStore
from django.core import serializers
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def index(request):
    #index페이지 로드할 때마다 세션에 값 넣는건 너무 비효율적인데...init을 따로 할 수 있나
    blog_info = Blog.objects.get(id=6)
    user = blog_info.user

    #get()은 하나의 결과값만 가져옴. 여러건을 가져올 땐 filter
    categories = Category.objects.filter(blog_id=blog_info.id)
    #base data
    user_info = {'nickname':user.nickname }
    category_list = [{'id':c.id,'name':c.name, 'count':Post.objects.filter(category_id=c.id).count()} for c in categories]
    request.session['blog_info'] = {'id':blog_info.id, 'blogname':blog_info.blogname }
    request.session['category_info'] = category_list
    request.session['user_info'] = user_info
    #index data
    paginator = Paginator(Post.objects.order_by('-reg_date'), 5)

    post_list = paginator.get_page(1)
    context = {
        'page': 1,
        'post_list' : post_list
    }
    template = loader.get_template('unknownstation/index.html')
    return HttpResponse(template.render(context, request))

def list(request,page):

    #index data
    paginator = Paginator(Post.objects.order_by('-reg_date'), 5)
    '''
    page = request.GET.get("page")
    '''
    if page is None:
        page = 1

    post_list = paginator.get_page(page)
    context = {
        'page': page,
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
    categories = Category.objects.filter(blog_id=request.session.get('blog_info')['id'])
    category_list = [{'id':c.id,'name':c.name, 'count':Post.objects.filter(category_id=c.id).count()} for c in categories]
    request.session['category_info'] = category_list
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
    categories = Category.objects.filter(blog_id=request.session.get('blog_info')['id'])
    category_list = [{'id':c.id,'name':c.name, 'count':Post.objects.filter(category_id=c.id).count()} for c in categories]
    request.session['category_info'] = category_list
    return HttpResponseRedirect(reverse('unknownstation:index'))

def login(request):
    form = LoginForm()
    return render(request, 'unknownstation/login.html', {'form':form})

def logout(request):
    request.session['nickname']=None
    request.session['user_id']=None
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

def byCategory(request, category_id, page):
    categories=request.session.get('category_info')
    #왜 session['category']로 가져오면 count값이 안나올까?
    category_info=None
    for c in categories:
        print(c)
        if c["id"]==category_id:
            category_info =c

    post_list = Post.objects.filter(category_id=category_id).order_by('-reg_date')
    paginator = Paginator(post_list, 5)
    post_list = paginator.get_page(page)
    return render(request, 'unknownstation/listByCategory.html', {'post_list':post_list, 'page':page, 'category':category_info})
