# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-16 11:00
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0035_streamfieldmigrationmodels'),
    ]

    operations = [
        migrations.AddField(
            model_name='addedstreamfieldwithemptylistdefaultpage',
            name='body',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.CharBlock())], default=[]),
        ),
        migrations.AddField(
            model_name='addedstreamfieldwithemptystringdefaultpage',
            name='body',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.CharBlock())], default=''),
        ),
        migrations.AddField(
            model_name='addedstreamfieldwithoutdefaultpage',
            name='body',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.CharBlock())], default=''),
            preserve_default=False,
        ),
    ]
