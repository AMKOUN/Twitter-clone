from django.shortcuts import render, get_object_or_404
from posts_app.models import Post, Group

def first(request):
    posts = Post.objects.select_related(
        'group', 'autor',
    ).order_by('-pub_date')
    context = {
        'posts' : posts
    }
    return render(request, 'posts_app/index.html', context)

def second(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related(
        'group'
    )
    context = {
        'posts' : posts,
        'group' : group
    }
    return render(request, 'posts_app/group_list.html', context)