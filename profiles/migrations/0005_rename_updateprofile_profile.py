# Generated by Django 5.0.6 on 2024-07-16 06:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_updateprofile_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UpdateProfile',
            new_name='Profile',
        ),
    ]
