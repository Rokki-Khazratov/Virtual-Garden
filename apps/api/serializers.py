from rest_framework import serializers
from apps.plants.models import Plants,UserProfile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class PlantSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()

    class Meta:
        model = Plants
        fields = ['id', 'name', 'info', 'img']

    def get_img(self, plant):
        request = self.context.get('request')
        if plant.img:
            return request.build_absolute_uri(plant.img.url)
        return None
