from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog


def allblogs(request, page):
    blogs = Blog.objects.all().order_by("-pub_date")
    pages = Paginator(blogs, 5)
    result_page = pages.page(page)
    return render(request, 'blog/allblogs.html', {'blogs': result_page})


def detail(request, slug):
    detailblog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog/detail.html', {'blog': detailblog})

