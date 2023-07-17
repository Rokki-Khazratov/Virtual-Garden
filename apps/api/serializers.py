from rest_framework import serializers
from apps.plants.models import Plants,UserProfile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        
class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plants
        fields = '__all__'