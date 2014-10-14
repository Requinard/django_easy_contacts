# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_last_modified', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('telephone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_last_modified', models.DateTimeField(auto_now_add=True)),
                ('industry_name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_last_modified', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contact',
            name='industry',
            field=models.ManyToManyField(to='contacts.Industry'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='type',
            field=models.ManyToManyField(to='contacts.Type'),
            preserve_default=True,
        ),
    ]
