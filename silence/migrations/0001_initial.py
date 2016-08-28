# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activateuserinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('countall', models.IntegerField(null=True, blank=True)),
                ('countactivate', models.IntegerField(null=True, blank=True)),
                ('unichg', models.IntegerField(null=True, blank=True)),
                ('smsmo', models.IntegerField(null=True, blank=True)),
                ('callduration', models.IntegerField(null=True, blank=True)),
                ('data', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'activateuserinfo',
            },
        ),
        migrations.CreateModel(
            name='Callhistory',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=50, null=True, blank=True)),
                ('calldate', models.DateTimeField(null=True, blank=True)),
                ('memo', models.TextField(null=True, blank=True)),
                ('imsi', models.BigIntegerField()),
            ],
            options={
                'db_table': 'callhistory',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null=True, blank=True)),
                ('score', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u6807\u7b7e',
                'verbose_name_plural': '\u6807\u7b7e',
            },
        ),
        migrations.CreateModel(
            name='Testuserout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('provcd', models.IntegerField(null=True, blank=True)),
                ('provnm', models.CharField(max_length=40, null=True, blank=True)),
                ('imsi', models.BigIntegerField(null=True, blank=True)),
                ('cdrall', models.BigIntegerField(null=True, blank=True)),
                ('cdrvoice', models.BigIntegerField(null=True, blank=True)),
                ('cdrdata', models.BigIntegerField(null=True, blank=True)),
                ('cdr23g', models.BigIntegerField(null=True, blank=True)),
                ('cdr4g', models.BigIntegerField(null=True, blank=True)),
                ('callduration', models.BigIntegerField(null=True, blank=True)),
                ('smsmo', models.BigIntegerField(null=True, blank=True)),
                ('smsmt', models.BigIntegerField(null=True, blank=True)),
                ('data', models.BigIntegerField(null=True, blank=True)),
                ('data23g', models.BigIntegerField(null=True, blank=True)),
                ('data4g', models.BigIntegerField(null=True, blank=True)),
                ('chgrmb', models.BigIntegerField(null=True, blank=True)),
                ('unichg', models.BigIntegerField(null=True, blank=True)),
                ('days', models.IntegerField(null=True, blank=True)),
                ('carriers', models.IntegerField(null=True, blank=True)),
                ('countrys', models.IntegerField(null=True, blank=True)),
                ('country_list', models.CharField(max_length=500, null=True, blank=True)),
                ('lastcalldt', models.IntegerField(null=True, blank=True)),
                ('issilence', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'ordering': ['-days', '-lastcalldt'],
                'db_table': 'testuserout',
            },
        ),
        migrations.CreateModel(
            name='Testuseroutold',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sttldt', models.IntegerField(null=True, blank=True)),
                ('callstartdt', models.IntegerField(null=True, blank=True)),
                ('carriercd', models.CharField(max_length=5, null=True, blank=True)),
                ('provcd', models.IntegerField(null=True, blank=True)),
                ('imsi', models.BigIntegerField(null=True, blank=True)),
                ('type', models.SmallIntegerField(null=True, blank=True)),
                ('data', models.BigIntegerField(null=True, blank=True)),
                ('cdr', models.IntegerField(null=True, blank=True)),
                ('provsdr', models.IntegerField(null=True, blank=True)),
                ('provrmb', models.IntegerField(null=True, blank=True)),
                ('carriercdr', models.IntegerField(null=True, blank=True)),
                ('carrierrmb', models.IntegerField(null=True, blank=True)),
                ('unichg', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'testuseroutold',
            },
        ),
    ]
