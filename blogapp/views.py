from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog_view(request):
    return render(request, 'blog/blog-home.html')


def blog_single(request):
    context = {'title': 'Blog Title', 'content': 'This is the content of the blog post.'}
    return render(request, 'blog/blog-single.html', context)
