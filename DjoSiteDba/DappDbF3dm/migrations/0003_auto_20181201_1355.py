# Generated by Django 2.1.1 on 2018-12-01 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DappDbF3dm', '0002_dct_t_l3f3dm_hour_report_aqyc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dct_t_l3f3dm_hour_report_aqyc',
            name='report_date',
            field=models.DateField(db_index=True, null=True),
        ),
    ]