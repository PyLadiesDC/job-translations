# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobtranslations', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='JobPost',
        ),
        migrations.RemoveField(
            model_name='nlp',
            name='paste',
        ),
        migrations.RenameField(
            model_name='paste',
            old_name='paster_email',
            new_name='email',
        ),
        migrations.DeleteModel(
            name='NLP',
        ),
    ]
