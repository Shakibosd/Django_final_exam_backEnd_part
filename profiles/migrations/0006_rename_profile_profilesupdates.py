# Generated by Django 5.0.6 on 2024-07-16 06:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_rename_updateprofile_profile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='ProfilesUpdates',
        ),
    ]
