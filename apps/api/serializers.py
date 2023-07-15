from rest_framework import serializers
from apps.plants.models import Plants,UserProfile


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plants
        fields = '__all__'