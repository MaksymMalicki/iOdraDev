# Generated by Django 3.1.3 on 2021-07-15 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainMap', '0004_chunk_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='chunk',
            name='viewBox',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
