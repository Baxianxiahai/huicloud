# Generated by Django 2.1a1 on 2018-08-30 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dct_t_l3fxprcm_locklog_fhys',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('woid', models.CharField(max_length=10)),
                ('site_code', models.IntegerField(default=0)),
                ('keyid', models.CharField(max_length=10)),
                ('keyname', models.CharField(max_length=20)),
                ('ownerid', models.CharField(max_length=15)),
                ('ownername', models.CharField(max_length=20)),
                ('eventtype', models.CharField(max_length=1)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('picname', models.CharField(max_length=100)),
            ],
        ),
    ]
