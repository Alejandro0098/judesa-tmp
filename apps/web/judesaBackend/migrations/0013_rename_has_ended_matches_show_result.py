# Generated by Django 5.1.1 on 2024-09-24 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judesaBackend', '0012_matches_location_alter_matches_rival_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matches',
            old_name='has_ended',
            new_name='show_result',
        ),
    ]
