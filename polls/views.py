from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
from .models import Article

def index(request):
    context={
        'title':'Home',
        'time':datetime.now()
    }
    return render(request,'polls/index.html',context)


def about(request):
    context={
        'title':'About',
        'time':datetime.now()
    }
    return render(request,'polls/about.html',context)

def news(request):
    Articles=Article.objects.all()
    context={
        'title':'News',
        'time':datetime.now(),
        'article':Articles
    }
    return render(request,'polls/news.html',context)





