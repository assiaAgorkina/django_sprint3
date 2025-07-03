from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category


def index(request):
    posts = Post.objects.select_related('category', 'author').filter(
        pub_date__lte=timezone.now(),  # Только с прошедшей датой публикации
        is_published=True,  # Только опубликованные
        category__is_published=True  # Только из опубликованных категорий
    ).order_by('-pub_date')[:5]  # Последние 5 постов
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    post = get_object_or_404(
        Post.objects.select_related('category', 'author'),
        pk=id,
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = Post.objects.select_related('author').filter(
        category=category,
        pub_date__lte=timezone.now(),
        is_published=True
    ).order_by('-pub_date')
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog/category.html', context)
