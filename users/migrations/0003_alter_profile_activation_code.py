# Generated by Django 5.0.6 on 2024-07-15 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_activation_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='activation_code',
            field=models.CharField(max_length=64),
        ),
    ]
