# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bares',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('direccion', models.CharField(max_length=50, unique=True)),
                ('num_visitas', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tapas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('votos', models.IntegerField(default=0)),
                ('bar', models.ForeignKey(to='DjangoApp1.Bares')),
            ],
        ),
    ]
