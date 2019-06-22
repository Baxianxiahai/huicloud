# Generated by Django 2.1.4 on 2019-04-18 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DappDbF2cm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dct_t_l3f2cm_nbiot_ctc_token',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('appid', models.CharField(max_length=256)),
                ('appsecret', models.CharField(max_length=256)),
                ('serviceid', models.CharField(max_length=256)),
                ('accesstoken', models.CharField(max_length=256)),
                ('refreshtoken', models.CharField(max_length=256)),
                ('accexpires', models.DateTimeField(max_length=0)),
                ('refexpires', models.DateTimeField(max_length=0)),
            ],
        ),
        migrations.AddField(
            model_name='dct_t_l3f2cm_device_cail',
            name='no2_coefB',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='dct_t_l3f2cm_device_cail',
            name='no2_coefK',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='dct_t_l3f2cm_device_cail',
            name='no2_coefmax',
            field=models.FloatField(default=20),
        ),
        migrations.AddField(
            model_name='dct_t_l3f2cm_device_cail',
            name='no2_coefmin',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='dct_t_l3f2cm_device_inventory',
            name='port_flag',
            field=models.BooleanField(default=True),
        ),
    ]