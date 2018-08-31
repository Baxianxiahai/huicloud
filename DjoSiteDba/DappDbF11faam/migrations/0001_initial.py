# Generated by Django 2.1a1 on 2018-08-30 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dct_t_l3f11faam_buy_consumables',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('supplier', models.CharField(max_length=50)),
                ('contype', models.CharField(max_length=10)),
                ('amount', models.IntegerField(default=0)),
                ('unitprice', models.DecimalField(decimal_places=3, max_digits=10)),
                ('totalprice', models.DecimalField(decimal_places=3, max_digits=10)),
                ('createtime', models.DateTimeField(null=True)),
                ('datatype', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f11faam_daily_sheet',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('pjcode', models.CharField(max_length=10)),
                ('employee', models.CharField(max_length=10)),
                ('workday', models.DateField(null=True)),
                ('arraytime', models.TimeField(null=True)),
                ('leavetime', models.TimeField(null=True)),
                ('offwork', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
                ('worktime', models.FloatField(null=True)),
                ('unitprice', models.IntegerField(null=True)),
                ('laterflag', models.BooleanField(default=False)),
                ('earlyflag', models.BooleanField(default=False)),
                ('daystandardnum', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f11faam_factory_sheet',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('pjcode', models.CharField(max_length=10)),
                ('workstart', models.TimeField(null=True)),
                ('workend', models.TimeField(null=True)),
                ('reststart', models.TimeField(null=True)),
                ('restend', models.TimeField(null=True)),
                ('fullwork', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=100)),
                ('latitude', models.IntegerField(default=0)),
                ('longitude', models.IntegerField(default=0)),
                ('trafficmoney', models.IntegerField(null=True)),
                ('factorybonus', models.IntegerField(null=True)),
                ('memo', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f11faam_material_history',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('stockid', models.CharField(max_length=10)),
                ('stockname', models.CharField(max_length=30)),
                ('into', models.BooleanField(default=False)),
                ('bucketnum', models.IntegerField(null=True)),
                ('price', models.IntegerField(null=True)),
                ('mode', models.BooleanField(default=False)),
                ('vendor', models.CharField(max_length=30, null=True)),
                ('charge', models.CharField(max_length=30, null=True)),
                ('mobile', models.CharField(max_length=15)),
                ('trunk', models.CharField(max_length=15, null=True)),
                ('target', models.CharField(max_length=30, null=True)),
                ('logisitics', models.CharField(max_length=10, null=True)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f11faam_material_stock_table',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('stockname', models.CharField(max_length=20)),
                ('stockaddress', models.CharField(max_length=100)),
                ('stockleader', models.CharField(max_length=10)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('isself', models.BooleanField(default=False)),
                ('bucketnum', models.IntegerField(default=0)),
                ('totalprice', models.IntegerField(default=0)),
                ('updatetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f11faam_member_sheet',
            fields=[
                ('mid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('pjcode', models.CharField(max_length=10)),
                ('employee', models.CharField(max_length=10)),
                ('gender', models.IntegerField(default=1)),
                ('phone', models.CharField(max_length=15)),
                ('openid', models.CharField(max_length=50)),
                ('regdate', models.DateField(auto_now_add=True)),
                ('position', models.CharField(max_length=10)),
                ('zone', models.CharField(max_length=50, null=True)),
                ('idcard', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100, null=True)),
                ('bank', models.CharField(max_length=10, null=True)),
                ('bankcard', models.CharField(max_length=20)),
                ('photo', models.CharField(max_length=15)),
                ('unitprice', models.IntegerField(default=0)),
                ('standardnum', models.IntegerField(default=0)),
                ('onjob', models.BooleanField(default=True)),
                ('memo', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f11faam_product_history',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('stockname', models.CharField(max_length=20)),
                ('productweight', models.IntegerField(default=0, null=True)),
                ('puoductsize', models.CharField(max_length=4, null=True)),
                ('productnum', models.IntegerField(default=0, null=True)),
                ('number', models.IntegerField(default=0, null=True)),
                ('containerID', models.CharField(max_length=30, null=True)),
                ('platenumber', models.IntegerField(default=0)),
                ('drivername', models.CharField(max_length=10)),
                ('driverphone', models.CharField(max_length=15)),
                ('receivingunit', models.CharField(max_length=15)),
                ('logisticsunit', models.CharField(max_length=20)),
                ('outtime', models.DateTimeField(auto_now=True)),
                ('message', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f11faam_product_stock_sheet',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('stockname', models.CharField(max_length=20)),
                ('stockaddress', models.CharField(max_length=50)),
                ('createtime', models.DateTimeField(null=True)),
                ('productweight', models.IntegerField(default=0, null=True)),
                ('puoductsize', models.CharField(max_length=4, null=True)),
                ('productnum', models.IntegerField(default=0, null=True)),
                ('number', models.IntegerField(default=0, null=True)),
                ('message', models.CharField(max_length=10, null=True)),
                ('updatetime', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f11faam_production',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('pjcode', models.CharField(max_length=10)),
                ('qrcode', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=10)),
                ('typecode', models.CharField(max_length=10)),
                ('applyweek', models.IntegerField(null=True)),
                ('applytime', models.DateTimeField(auto_now_add=True)),
                ('activetime', models.DateTimeField(null=True)),
                ('activeman', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f11faam_type_sheet',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('pjcode', models.CharField(default='HYGS', max_length=10)),
                ('typecode', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('applenum', models.IntegerField(default=0)),
                ('appleweight', models.DecimalField(decimal_places=1, max_digits=3)),
                ('applegrade', models.CharField(blank=True, max_length=1, null=True)),
                ('memo', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
