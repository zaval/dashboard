# Generated by Django 2.2.1 on 2019-05-17 17:02

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0002_parsetask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parsetask',
            name='result',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, null=True),
        ),
    ]
