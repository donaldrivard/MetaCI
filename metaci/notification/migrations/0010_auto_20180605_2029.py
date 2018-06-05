# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-05 20:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0009_auto_20180605_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchnotification',
            name='target',
            field=models.ForeignKey(db_column='branch_id', on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='repository.Branch', verbose_name='branch'),
        ),
        migrations.AlterField(
            model_name='plannotification',
            name='target',
            field=models.ForeignKey(db_column='plan_id', on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='plan.Plan', verbose_name='plan'),
        ),
        migrations.AlterField(
            model_name='planrepositorynotification',
            name='target',
            field=models.ForeignKey(db_column='planrepository_id', on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='plan.PlanRepository', verbose_name='planrepository'),
        ),
        migrations.AlterField(
            model_name='repositorynotification',
            name='target',
            field=models.ForeignKey(db_column='repo_id', on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='repository.Repository', verbose_name='repo'),
        ),
    ]