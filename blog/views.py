from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Post, Comment
from .forms import CommentForm, PostForm, LoginForm

# Create your views here.
def index(request):
    latest_blog_posts = Post.objects.order_by('-created')[:5]
    return render(request, 'blog/index.html', {'posts': latest_blog_posts})

def view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.get_post_comments_published()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        # validate form
        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = Post.objects.get(pk=post_id)
            obj.save()

    else:
        form = CommentForm()

    return render(request, 'blog/view.html', {
        'post': post,
        'comments': comments,
        'commentform': form
        })

def profile(request):
    current_user = request.user
    return render(request, 'blog/profile.html', {'user': current_user})

def newpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            user = request.user

            obj = form.save(commit=False)
            obj.owner = User.objects.get(pk=user.id)
            obj.save()
    else:
        form = PostForm()
    return render(request, 'blog/newpost.html', {
        'postform': form
        })

def postcomments(request):
    user = request.user
    posts = Post.objects.filter(owner__id__exact=user.id)
    comments = []
    for post in posts:
        post_comments = post.get_post_comments_all()
        comments.append(post_comments)
    return render(request, 'blog/postcomments.html', {
        'comments': comments,
        'posts': posts
        })

def posts_by_tag(request, slug):
    posts = Post.objects.filter(tags__name__iexact=slug)
    return render(request, 'blog/posts_by_tag.html', {
        'posts': posts,
        'slug': slug
        })

def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/blog')
            else:
                return HttpResponse('Your account is not activated')
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'loginform': form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/blog')
