# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20150114_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='estimation',
            field=models.FloatField(blank=True, null=True, default=None, verbose_name='estimation'),
            preserve_default=True,
        ),
    ]
