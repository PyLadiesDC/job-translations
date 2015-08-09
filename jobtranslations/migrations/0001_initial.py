# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='NLP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_description', models.TextField()),
                ('job_qualifications', models.TextField()),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('paster_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='nlp',
            name='paste',
            field=models.ForeignKey(to='jobtranslations.Paste'),
        ),
    ]
