# Generated by Django 5.1.1 on 2024-09-24 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judesaBackend', '0013_rename_has_ended_matches_show_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
