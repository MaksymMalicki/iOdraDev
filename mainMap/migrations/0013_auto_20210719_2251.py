# Generated by Django 3.1.3 on 2021-07-19 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainMap', '0012_auto_20210719_2228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chunk',
            name='next',
        ),
        migrations.RemoveField(
            model_name='chunk',
            name='prev',
        ),
    ]
