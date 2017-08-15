from django.shortcuts import render

from blog.models import Users
from django.http import HttpResponse



def index(request):
  return render(request, 'index.html',{'name':None})


def login(request):
    username = request.GET['username']
    passwd = request.GET['password']
    print(passwd)
    print(Users.objects.get(name=username))
    if str(Users.objects.get(name=username))== passwd:
#    passwd = request.GET['blog_passwd',None]
      return render(request, 'index.html', {'name': username})
    else: 
      return render(request, 'error.html') 

def toLogin(request):
    return render(request, 'login.html')
    
# Create your views here.
