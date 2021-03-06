# Generated by Django 3.1.3 on 2021-07-22 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainMap', '0014_auto_20210719_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jaz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('localization', models.CharField(max_length=30)),
                ('description', models.TextField(default='')),
                ('state', models.BooleanField(default=True)),
                ('x_pos', models.IntegerField(default=0)),
                ('y_pos', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('chunk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jaz', to='mainMap.chunk')),
            ],
        ),
    ]
