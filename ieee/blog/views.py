from django.shortcuts import render
from blog.models import Post


def blog(request):
    posts = Post.get_posts()

    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)


def post(request, id):
    post = Post.get_post(id)

    context = {
        'post': post,
    }

    return render(request, 'blog/post.html', context)
