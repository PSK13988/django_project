from django.shortcuts import render
from .models import Post

def home(request):
    return render(request, 'blog/home.html', {'title':'Pankaj Kharche', 'posts': Post.objects.all()})

def about(request):
    return render(request, 'blog/about.html', {})