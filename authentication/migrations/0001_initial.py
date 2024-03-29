# Generated by Django 5.0.2 on 2024-02-23 09:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('language', models.CharField(blank=True, max_length=100, null=True)),
                ('religion', models.CharField(blank=True, max_length=100, null=True)),
                ('region_of_residence', models.CharField(blank=True, max_length=100, null=True)),
                ('tribe', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='authentication_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
