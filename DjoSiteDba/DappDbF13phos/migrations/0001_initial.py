# Generated by Django 2.1.4 on 2019-04-17 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dct_t_l3f13phos_account_info',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('account_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f13phos_app_user_info',
            fields=[
                ('uid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=10, null=True)),
                ('utelephone', models.CharField(max_length=11)),
                ('vercode', models.IntegerField(default=None, null=True)),
                ('vertime', models.DateTimeField(default=None, max_length=0, null=True)),
                ('idnumber', models.CharField(max_length=20, null=True)),
                ('openid', models.CharField(max_length=50)),
                ('user_type', models.IntegerField(default=1)),
                ('driver_code', models.CharField(default=None, max_length=20, null=True)),
                ('driver_status', models.IntegerField(default=3)),
                ('id_positive', models.CharField(default=None, max_length=100, null=True)),
                ('id_side', models.CharField(default=None, max_length=100, null=True)),
                ('drive_img', models.CharField(default=None, max_length=100, null=True)),
                ('trans_img', models.CharField(default=None, max_length=100, null=True)),
                ('trans_code', models.CharField(default=None, max_length=100, null=True)),
                ('longitude', models.DecimalField(decimal_places=6, default=0, max_digits=10)),
                ('latitude', models.DecimalField(decimal_places=6, default=0, max_digits=10)),
                ('regitime', models.DateTimeField(max_length=0)),
                ('info_status', models.BooleanField(default=False)),
                ('driver_type', models.IntegerField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f13phos_company_data_day',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('data_day', models.DateField(default=None, null=True)),
                ('pound', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f13phos_company_data_mounth',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('mounth_start', models.DateField(default=None, null=True)),
                ('mounth_end', models.DateField(default=None, null=True)),
                ('pound', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f13phos_company_info',
            fields=[
                ('com_code', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('business_img', models.CharField(max_length=100)),
                ('business_code', models.CharField(max_length=50)),
                ('com_name', models.CharField(max_length=100)),
                ('com_repre', models.CharField(max_length=10)),
                ('com_time', models.DateField(default=None, null=True)),
                ('com_address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f13phos_contract',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('contname', models.CharField(max_length=100)),
                ('txt_1', models.TextField(default=None, null=True)),
                ('txt_2', models.TextField(default=None, null=True)),
                ('txt_3', models.TextField(default=None, null=True)),
                ('contstatus', models.BooleanField(default=True)),
                ('com_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DappDbF13phos.dct_t_l3f13phos_company_info')),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f13phos_goods_info',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('goods_name', models.CharField(max_length=25)),
                ('goods_length', models.FloatField(default=0)),
                ('goods_height', models.FloatField(default=0)),
                ('goods_width', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f13phos_route',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('reporttime', models.DateTimeField(max_length=0)),
                ('longitude', models.DecimalField(decimal_places=6, default=None, max_digits=10, null=True)),
                ('latitude', models.DecimalField(decimal_places=6, default=None, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f13phos_task',
            fields=[
                ('task_code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('start_date', models.DateTimeField(default=None, max_length=0, null=True)),
                ('arrive_time', models.DateTimeField(default=None, max_length=0, null=True)),
                ('sprovince', models.CharField(max_length=10)),
                ('scity', models.CharField(max_length=30)),
                ('scounty', models.CharField(max_length=30)),
                ('saddress', models.CharField(max_length=100)),
                ('eprovince', models.CharField(max_length=10)),
                ('ecity', models.CharField(max_length=30)),
                ('ecounty', models.CharField(max_length=30)),
                ('eaddress', models.CharField(max_length=100)),
                ('task_status', models.IntegerField(default=0)),
                ('weight', models.FloatField(default=0)),
                ('price', models.FloatField(default=0)),
                ('lpound', models.FloatField(default=0)),
                ('upound', models.FloatField(default=0)),
                ('load_img', models.CharField(default=None, max_length=100, null=True)),
                ('unload_img', models.CharField(default=None, max_length=100, null=True)),
                ('load_date', models.DateTimeField(default=None, null=True)),
                ('unload_date', models.DateTimeField(default=None, null=True)),
                ('longitude', models.DecimalField(decimal_places=6, default=None, max_digits=10, null=True)),
                ('latitude', models.DecimalField(decimal_places=6, default=None, max_digits=10, null=True)),
                ('ulongitude', models.DecimalField(decimal_places=6, default=None, max_digits=10, null=True)),
                ('ulatitude', models.DecimalField(decimal_places=6, default=None, max_digits=10, null=True)),
                ('com_code', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='DappDbF13phos.dct_t_l3f13phos_company_info')),
                ('contcode', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='DappDbF13phos.dct_t_l3f13phos_contract')),
                ('driver', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='driver_user', to='DappDbF13phos.dct_t_l3f13phos_app_user_info')),
                ('goods_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DappDbF13phos.dct_t_l3f13phos_goods_info')),
                ('load_account', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='load_account', to='DappDbF13phos.dct_t_l3f13phos_account_info')),
                ('manage', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manage_user', to='DappDbF13phos.dct_t_l3f13phos_app_user_info')),
                ('unload_account', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unload_account', to='DappDbF13phos.dct_t_l3f13phos_account_info')),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f13phos_user_car',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('car_type', models.IntegerField(default=0)),
                ('car_img', models.CharField(max_length=100)),
                ('car_plate', models.CharField(max_length=20, unique=True)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DappDbF13phos.dct_t_l3f13phos_app_user_info')),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f13phos_user_company',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('ustatus', models.IntegerField(default=0)),
                ('com_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DappDbF13phos.dct_t_l3f13phos_company_info')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DappDbF13phos.dct_t_l3f13phos_app_user_info')),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f13phos_user_data_day',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('data_day', models.DateField(default=None, null=True)),
                ('pound', models.FloatField(default=0)),
                ('price', models.FloatField(default=0)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DappDbF13phos.dct_t_l3f13phos_app_user_info')),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f13phos_user_data_mounth',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('mounth_start', models.DateField(default=None, null=True)),
                ('mounth_end', models.DateField(default=None, null=True)),
                ('pound', models.FloatField(default=0)),
                ('price', models.FloatField(default=0)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DappDbF13phos.dct_t_l3f13phos_app_user_info')),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f13phos_video',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('vtime', models.DateTimeField(max_length=0)),
                ('vtype', models.IntegerField(default=0)),
                ('vname', models.CharField(max_length=30)),
                ('vpath', models.CharField(max_length=100)),
                ('longitude', models.DecimalField(decimal_places=6, default=None, max_digits=10, null=True)),
                ('latitude', models.DecimalField(decimal_places=6, default=None, max_digits=10, null=True)),
                ('task_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DappDbF13phos.dct_t_l3f13phos_task')),
            ],
        ),
        migrations.AddField(
            model_name='dct_t_l3f13phos_route',
            name='taskcode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DappDbF13phos.dct_t_l3f13phos_task'),
        ),
        migrations.AddField(
            model_name='dct_t_l3f13phos_route',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DappDbF13phos.dct_t_l3f13phos_app_user_info'),
        ),
        migrations.AddField(
            model_name='dct_t_l3f13phos_company_data_mounth',
            name='com_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DappDbF13phos.dct_t_l3f13phos_company_info'),
        ),
        migrations.AddField(
            model_name='dct_t_l3f13phos_company_data_day',
            name='com_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DappDbF13phos.dct_t_l3f13phos_company_info'),
        ),
    ]
