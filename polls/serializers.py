from rest_framework import serializers
from polls.models import World

class WorldSerializer(serializers.Serializer):
	world_id = serializers.IntegerField(read_only=True)
	world_name = serializers.CharField()

#	def create():
#		"""
#		Return World
#		"""
#		return World.objects.all()