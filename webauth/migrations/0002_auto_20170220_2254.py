# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 20:54
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authtoken',
            name='key',
            field=models.TextField(max_length=60, verbose_name='Key'),
        ),
        migrations.AlterField(
            model_name='emailtoken',
            name='key',
            field=models.TextField(verbose_name='Key'),
        ),
        migrations.AlterField(
            model_name='passwordresettoken',
            name='key',
            field=models.TextField(verbose_name='Key'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.TextField(unique=True, validators=[django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(32)]),
        ),
    ]