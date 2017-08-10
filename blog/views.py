from django.shortcuts import render

from blog.models import Article
from django.http import HttpResponse



def index(request):
 
  name = Article.objects.get(title="root");
  return render(request, 'index.html',{'data':name});


def check(request):
    username = request.GET['blog_username']
    if username=='547187896@qq.com':
#    passwd = request.GET['blog_passwd',None]
      return render(request, 'home.html', {'name': username})
    else: 
      return render(request, 'error.html') 

    
# Create your views here.
