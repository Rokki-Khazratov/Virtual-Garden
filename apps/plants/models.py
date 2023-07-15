import os
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

def get_plant_photo_path(instance, filename):
    today = datetime.now()
    path = f'plants/{today.year}/{today.month}/{today.day}/'
    return os.path.join(path, filename)

class Plants(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField()
    img = models.ImageField(upload_to=get_plant_photo_path)
    
    def __str__(self):
        return self.name

class PlantImage(models.Model):
    plant = models.ForeignKey(Plants, default=None, on_delete=models.CASCADE)
    img = models.ImageField(upload_to=get_plant_photo_path)

    def __str__(self):
        return self.plant.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.SlugField(max_length=255, unique=True, null=False)
    plants = models.ManyToManyField(Plants, related_name='user_profiles', blank=True)
    card = models.ManyToManyField(Plants, related_name='user_cards', blank=True)

    def __str__(self):
        return self.username
