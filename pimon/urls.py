"""pimon URL Configuration

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
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
	url(r'^admin/', admin.site.urls),
    url(r'^returnfeedback/(?P<id>[0-9])/$', views.returnfeedback, name='returnfeedback'),
    url(r'^confighome/', views.confighome, name='confighome'),
    url(r'^configglobal', views.configglobal, name='configglobal'),
	url(r'^myrigs/$', views.myrigs, name='myrigs'),
    url(r'^myrigs/addrig/$', views.addrig, name='addrig'),
    url(r'^myrigs/editrig/(?P<pk>[0-9]{1,10})/$', views.editrig, name='editrig'),
    url(r'^myrigs/delrig/(?P<pk>[0-9]{1,10})/$', views.delrig, name='delrig'),
]
