# Generated by Django 5.1.1 on 2024-09-24 18:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judesaBackend', '0019_staff_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='trainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trainer_id', to='judesaBackend.staff'),
        ),
    ]
