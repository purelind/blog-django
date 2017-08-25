from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'blog/index.html', context={
        'title': 'My blog index page',
        'welcome': 'Welcome to my blog index page.'
    })
