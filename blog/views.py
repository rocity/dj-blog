from django.shortcuts import render, get_object_or_404

from .models import Post, Comment

# Create your views here.
def index(request):
    latest_blog_posts = Post.objects.order_by('-created')[:5]
    return render(request, 'blog/index.html', {'posts': latest_blog_posts})

def view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(
        status__exact='published'
        ).order_by('-created')[:5]
    return render(request, 'blog/view.html', {
        'post': post,
        'comments': comments
        })
