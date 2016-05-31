from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.hello, name='hello'),
    url(r'^worlds/$', "polls.views.worlds", name='worlds'),
]