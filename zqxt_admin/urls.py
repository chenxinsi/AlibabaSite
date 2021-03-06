"""zqxt_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^$', views.index),
    url(r'toLogin',views.toLogin),
    url(r'toRegister',views.toRegister),
    url(r'register',views.register),
    url(r'login/', views.login, name='login'),
    #url(r'next/', views.next, name='next'),
    url(r'^admin/', admin.site.urls),
] #+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

# if settings.DEBUG is False:   #if DEBUG is True it will be served automatically
#     urlpatterns += urlpatterns('',
#             url(r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
#     )

handler404 = views.page_not_found
