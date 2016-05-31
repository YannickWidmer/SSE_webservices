from django.shortcuts import render
from django.http import HttpResponse
from polls.models import World
from django.core import serializers


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def hello(request):
    return HttpResponse('hello')
def worlds(request):
    worlds = World.objects.all()
    data = serializers.serialize("json", worlds)
    return HttpResponse(data)
# Create your views here.
