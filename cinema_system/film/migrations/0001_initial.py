# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('rating', models.PositiveIntegerField(default=0)),
                ('priceOfTheThicket', models.PositiveIntegerField(default=0)),
                ('language', models.CharField(max_length=20)),
                ('time', models.PositiveIntegerField(default=0)),
                ('category', models.CharField(max_length=20)),
                ('subtitles', models.BooleanField(default=False)),
                ('age', models.PositiveIntegerField(default=0)),
                ('typeOfFilm', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
