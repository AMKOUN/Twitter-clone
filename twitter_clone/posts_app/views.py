from django.shortcuts import render
from posts_app.models import Post

def first(request):
    posts = Post.objects.select_related(
        'group', 'autor',
    )
    context = {
        'posts' : posts
    }
    return render(request, 'posts_app/index.html', context)