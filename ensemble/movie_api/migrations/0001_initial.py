# Generated by Django 4.0 on 2021-12-18 23:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=500)),
                ('release_year', models.DateField()),
                ('duration', models.DurationField()),
                ('rating', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('likes', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['release_year'],
                'unique_together': {('title', 'release_year')},
            },
        ),
    ]