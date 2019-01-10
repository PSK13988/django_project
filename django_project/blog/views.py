from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts=[{
    'author':'Pankaj Kharche',
    'title':'First Blog post',
    'content':'This is my First Blog message',
    'date_posted':'January 10, 2019'
},{
    'author':'Jagruti Kharche',
    'title':'Second Blog post',
    'content':'This is my Second Blog message',
    'date_posted':'January 11, 2019'
}]


def home(request):
    return render(request, 'blog/home.html', {'title':'Pankaj Kharche', 'posts': posts})

def about(request):
    return render(request, 'blog/about.html', {})