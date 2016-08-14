# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0004_auto_20160717_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='head_img',
            field=models.ImageField(upload_to=b'uploads'),
        ),
    ]
