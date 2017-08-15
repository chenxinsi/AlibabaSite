from django.shortcuts import render
from django.shortcuts import render_to_response
from blog.models import Users
from django.http import HttpResponse


keys = ('id','name','passwd')
def page_not_found(request):
    return render_to_response('error.html')

def index(request):
  userdata = Users.objects.all().values_list('id', 'name', 'passwd')
  return render(request, 'index.html',{'name':None,'userdata':userdata,'keys':keys})


def login(request):
    username = request.GET['username']
    passwd = request.GET['password']
    print(passwd)
    print(Users.objects.get(name=username))
    userdata = Users.objects.all().values_list('id','name','passwd')
    if str(Users.objects.get(name=username))== passwd:
#    passwd = request.GET['blog_passwd',None]
      return render(request, 'index.html', {'name': username,'userdata':userdata,'keys':keys})
    else: 
      return render(request, 'error.html') 

def toLogin(request):
    return render(request, 'login.html')

def toRegister(request):
    return render(request, 'register.html')

def register(request):
    userdata = Users.objects.all().values_list('id', 'name', 'passwd')
    username = request.GET['username']
    passwd = request.GET['password']
    if passwd in str(Users.objects.all().values_list('passwd')):
        print("yes")
    Users.objects.create(name=username,passwd=passwd)
    if str(Users.objects.get(name=username)) == passwd:
       return render(request, "index.html",{'name':username,'userdata':userdata,'keys':keys})
    else:
        print("注册 数据库导入数据失败")
# Create your views here.
