# Generated by Django 5.0.6 on 2024-07-15 12:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0002_alter_flower_category_alter_flower_title_and_more'),
        ('orders', '0003_flower_alter_order_flower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='flower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flowers.flower'),
        ),
        migrations.DeleteModel(
            name='Flower',
        ),
    ]
