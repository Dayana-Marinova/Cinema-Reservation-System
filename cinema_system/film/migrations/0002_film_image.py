# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='image',
            field=models.ImageField(default=datetime.date(2014, 6, 2), upload_to='images/filmthumbs/'),
            preserve_default=False,
        ),
    ]
