# Generated by Django 5.0.3 on 2024-03-15 01:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0005_alter_pto_request_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pto_request',
            name='to',
        ),
        migrations.AddField(
            model_name='pto_request',
            name='pto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='track.pto_type'),
        ),
        migrations.AddField(
            model_name='pto_request',
            name='send_to',
            field=models.CharField(max_length=30, null=True, verbose_name='supervisorsemail@email1.com, supervisorsemail@email2.com'),
        ),
        migrations.AlterField(
            model_name='pto_request',
            name='date_requested',
            field=models.CharField(max_length=120, verbose_name='For what dates (MM/DD/TT): '),
        ),
        migrations.AlterField(
            model_name='pto_request',
            name='hours_used',
            field=models.CharField(max_length=2, verbose_name='Total hours requested: '),
        ),
        migrations.AlterField(
            model_name='pto_request',
            name='notes',
            field=models.CharField(blank=True, max_length=120, verbose_name='Notes: '),
        ),
        migrations.AlterField(
            model_name='pto_request',
            name='pto_type',
            field=models.CharField(max_length=3, verbose_name='What are you using: '),
        ),
    ]