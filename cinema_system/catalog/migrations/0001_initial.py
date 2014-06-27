# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('default', models.BooleanField(default=True)),
                ('comedy', models.BooleanField(default=False)),
                ('thriller', models.BooleanField(default=False)),
                ('romantic', models.BooleanField(default=False)),
                ('animation', models.BooleanField(default=False)),
                ('drama', models.BooleanField(default=False)),
                ('criminal', models.BooleanField(default=False)),
                ('historical', models.BooleanField(default=False)),
                ('documentary', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
