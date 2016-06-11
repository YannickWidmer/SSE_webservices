from django.conf.urls import url

from rest_framework.authtoken import views as tokenviews
from . import views

#from rest_framework.authtoken import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.hello, name='hello'),
    url(r'^worlds/$', views.WorldList.as_view()),
    url(r'^api-token-auth/', tokenviews.obtain_auth_token),
   # url(r'^api-token-auth/', views.obtain_auth_token),
]