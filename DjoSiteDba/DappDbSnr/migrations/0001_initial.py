# Generated by Django 2.1a1 on 2018-07-16 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('DappDbF2cm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dct_t_l2snr_dust',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('tsp', models.FloatField(blank=True, default=0, verbose_name='TSP')),
                ('pm01', models.FloatField(blank=True, default=0, verbose_name='PM0.1')),
                ('pm25', models.FloatField(blank=True, default=0, verbose_name='PM2.5')),
                ('pm10', models.FloatField(blank=True, default=0, verbose_name='PM10')),
                ('dataflag', models.CharField(max_length=1)),
                ('report_data', models.DateTimeField(auto_now=True)),
                ('hourminindex', models.IntegerField(default=0)),
                ('dev_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DappDbF2cm.dct_t_l3f2cm_device_common')),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l2snr_humidity',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('humidity', models.FloatField(blank=True, default=0, verbose_name='湿度值')),
                ('dataflag', models.CharField(max_length=1)),
                ('report_data', models.DateTimeField(auto_now=True)),
                ('hourminindex', models.IntegerField(default=0)),
                ('dev_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DappDbF2cm.dct_t_l3f2cm_device_common')),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l2snr_noise',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('noise', models.FloatField(blank=True, default=0, verbose_name='噪声')),
                ('dataflag', models.CharField(max_length=1)),
                ('report_data', models.DateTimeField(auto_now=True)),
                ('hourminindex', models.IntegerField(default=0)),
                ('dev_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DappDbF2cm.dct_t_l3f2cm_device_common')),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l2snr_picture',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('file_name', models.TextField(max_length=100)),
                ('file_size', models.IntegerField(default=0)),
                ('description', models.TextField(max_length=100)),
                ('dataflag', models.CharField(max_length=1)),
                ('report_data', models.DateTimeField(auto_now=True)),
                ('hourminindex', models.IntegerField(default=0)),
                ('site_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DappDbF2cm.dct_t_l3f2cm_site_common')),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l2snr_sensor_type',
            fields=[
                ('snr_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('snr_name', models.CharField(max_length=15)),
                ('value_min', models.FloatField(blank=True, default=0, verbose_name='量程最小值')),
                ('value_max', models.FloatField(blank=True, default=0, verbose_name='量程最大值')),
                ('snr_model', models.CharField(max_length=20)),
                ('snr_vendor', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l2snr_temperature',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('temperature', models.FloatField(blank=True, default=0, verbose_name='温度值')),
                ('dataflag', models.CharField(max_length=1)),
                ('report_data', models.DateTimeField(auto_now=True)),
                ('hourminindex', models.IntegerField(default=0)),
                ('dev_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DappDbF2cm.dct_t_l3f2cm_device_common')),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l2snr_winddir',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('windir', models.FloatField(blank=True, default=0, verbose_name='风向')),
                ('dataflag', models.CharField(max_length=1)),
                ('report_data', models.DateTimeField(auto_now=True)),
                ('hourminindex', models.IntegerField(default=0)),
                ('dev_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DappDbF2cm.dct_t_l3f2cm_device_common')),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l2snr_windspd',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('windspd', models.FloatField(blank=True, default=0, verbose_name='风速')),
                ('dataflag', models.CharField(max_length=1)),
                ('report_data', models.DateTimeField(auto_now=True)),
                ('hourminindex', models.IntegerField(default=0)),
                ('dev_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DappDbF2cm.dct_t_l3f2cm_device_common')),
            ],
        ),
    ]