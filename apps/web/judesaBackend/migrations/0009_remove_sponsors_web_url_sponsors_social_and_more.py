# Generated by Django 5.1.1 on 2024-09-18 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judesaBackend', '0008_news_tags_delete_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsors',
            name='web_url',
        ),
        migrations.AddField(
            model_name='sponsors',
            name='social',
            field=models.JSONField(default={}),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sponsors',
            name='image',
            field=models.CharField(default='', max_length=150, unique=True),
            preserve_default=False,
        ),
    ]
