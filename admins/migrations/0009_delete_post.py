# Generated by Django 5.0.6 on 2024-08-18 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0008_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]