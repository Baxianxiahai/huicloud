# Generated by Django 2.1.1 on 2018-11-23 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DappDbF11faam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dct_t_l3f11faam_batch_scan',
            name='applydate',
            field=models.DateTimeField(null=True),
        ),
    ]
