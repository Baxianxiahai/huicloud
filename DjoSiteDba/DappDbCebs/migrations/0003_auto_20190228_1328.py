# Generated by Django 2.1.7 on 2019-02-28 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DappDbCebs', '0002_auto_20190228_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_cebs_object_profile',
            name='objname',
            field=models.CharField(db_index=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='t_cebs_result_eleg',
            name='file_attr',
            field=models.IntegerField(db_index=True, default=1),
        ),
        migrations.AlterField(
            model_name='t_cebs_result_eleg',
            name='rec_time',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='t_cebs_user_sheet',
            name='login_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='t_cebs_user_sheet',
            name='memo',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
