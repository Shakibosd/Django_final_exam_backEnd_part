# Generated by Django 5.0.6 on 2024-08-20 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0023_alter_flower_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='image',
            field=models.CharField(default=''),
        ),
    ]
