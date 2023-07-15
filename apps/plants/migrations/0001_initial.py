# Generated by Django 4.2.3 on 2023-07-15 13:05

import apps.plants.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('info', models.TextField()),
                ('img', models.ImageField(upload_to=apps.plants.models.get_plant_photo_path)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.SlugField(max_length=255, unique=True)),
                ('card', models.ManyToManyField(blank=True, related_name='user_cards', to='plants.plants')),
                ('plants', models.ManyToManyField(blank=True, related_name='user_profiles', to='plants.plants')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlantImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=apps.plants.models.get_plant_photo_path)),
                ('plant', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='plants.plants')),
            ],
        ),
    ]