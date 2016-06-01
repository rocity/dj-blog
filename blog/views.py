from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post, Comment
from .forms import CommentForm

# Create your views here.
def index(request):
    latest_blog_posts = Post.objects.order_by('-created')[:5]
    return render(request, 'blog/index.html', {'posts': latest_blog_posts})

def view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(
        status__exact='published'
        ).order_by('-created')[:5]

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
