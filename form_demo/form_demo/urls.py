"""form_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from form import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add/$', views.add, name='add'),
    url(r'^update/(?P<id>\d+)/$', views.update, name='update'),
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^add2/$', views.add2, name='add2'),
    url(r'^feedback2/$', views.feedback2, name='feedback2'),
    url(r'^update2/(?P<id>\d+)/$', views.update2, name='update2'),
]
