# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobtranslations', '0002_auto_20150809_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasteJobURL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_URL', models.URLField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('email', models.EmailField(max_length=254, blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Paste',
        ),
    ]
