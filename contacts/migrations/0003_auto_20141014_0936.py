# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20141014_0934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='industry',
            old_name='industry_name',
            new_name='name',
        ),
    ]
