from django.shortcuts import render

from blog.models import Users
from django.http import HttpResponse



def index(request):
  return render(request, 'index.html');


def login(request):
    username = request.GET['username']
    passwd = request.GET['password']
    print(passwd)
    print(Users.objects.get(name=username))
    if str(Users.objects.get(name=username))== passwd:
#    passwd = request.GET['blog_passwd',None]
      return render(request, 'home.html', {'name': username})
    else: 
      return render(request, 'error.html') 

    
# Create your views here.
