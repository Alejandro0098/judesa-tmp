# Generated by Django 5.1.1 on 2024-09-23 20:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judesaBackend', '0009_remove_sponsors_web_url_sponsors_social_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_id_players', to='judesaBackend.categories'),
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rival', models.CharField(max_length=150, unique=True)),
                ('rival_score', models.PositiveIntegerField(default=0)),
                ('judesa_score', models.PositiveIntegerField(default=0)),
                ('match_date', models.DateTimeField()),
                ('is_local', models.BooleanField(default=True)),
                ('has_ended', models.BooleanField(default=False)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_id_matches', to='judesaBackend.categories')),
            ],
            options={
                'db_table': 'Matches',
            },
        ),
    ]
