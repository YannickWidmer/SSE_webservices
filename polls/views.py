from django.shortcuts import render
from polls.models import World
from polls.serializers import WorldSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def hello(request):
    return HttpResponse('hello')

class WorldList(APIView):
    """
    List all Worlds, or create a new snippet.
    """
    def get(self, request, format=None):
        worlds = World.objects.all()
        serializer = WorldSerializer(worlds, many=True)
        return Response(serializer.data)

   

# Create your views here.

