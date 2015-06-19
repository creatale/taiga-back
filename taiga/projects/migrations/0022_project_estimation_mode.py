# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_auto_20150504_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='estimation_mode',
            field=models.IntegerField(default=1, choices=[(1, 'User Story Estimation'), (2, 'Task Estimation')]),
            preserve_default=True,
        ),
    ]
