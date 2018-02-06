"""homelyProperties URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from homelyPropertiesapp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login_user,name="login"),
    url(r'^ownerdashboard/$',ownerdashboard,  name="ownerdashboard"),
    url(r'^register$',            register,         name="register"),
    url(r'^registerVisitor$',     register_visitor, name="registerVis"),
    url(r'^logout$',              logout_user,      name="logout"),
    url(r'^editProperties/(?P<pk>\d+)/$', editProperties, name='editProperties'),    
    url(r'^deleteProperties/(?P<pk>\d+)/$', deleteProperties, name='deleteProperties'),    
    url(r'^addProperties/$',ownerdashboard,  name="addProperties"),    
    url(r'^visitordashboard/$',visitordashboard,  name="visitordashboard"),
    url(r'^bookproperty/(?P<id>\d+)/$',bookproperty,  name="bookproperty"),
]
