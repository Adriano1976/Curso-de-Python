from django.shortcuts import render
from blog.models import Post


# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def h_posts(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    return render(request, 'posts.html', {'post': post})
