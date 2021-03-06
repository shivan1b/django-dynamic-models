# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-08 05:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('insurer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='risks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'risks',
                'default_related_name': 'risks',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='RiskField',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('ftype', models.CharField(choices=[('ch', 'String'), ('in', 'Integer'), ('dt', 'DateTime'), ('en', 'Choices')], help_text='Type of the field.', max_length=2)),
                ('risk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='riskfields', to='risk.Risk')),
            ],
            options={
                'db_table': 'riskfields',
                'default_related_name': 'riskfields',
                'ordering': ['-created'],
            },
        ),
    ]
