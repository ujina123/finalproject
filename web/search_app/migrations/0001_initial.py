# Generated by Django 4.0.4 on 2022-05-02 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plants',
            fields=[
                ('plantid', models.AutoField(db_column='plantId', primary_key=True, serialize=False)),
                ('url', models.CharField(db_column='URL', max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('botanynm', models.CharField(db_column='botanyNm', max_length=255)),
                ('info', models.TextField()),
                ('watercycle', models.CharField(db_column='waterCycle', max_length=255)),
                ('waterinfo', models.CharField(db_column='waterInfo', max_length=255)),
                ('waterexp', models.CharField(db_column='waterExp', max_length=255)),
                ('waterexpinfo', models.TextField(db_column='waterExpInfo')),
                ('light', models.CharField(max_length=255)),
                ('lightinfo', models.CharField(db_column='lightInfo', max_length=255)),
                ('lightexp', models.CharField(db_column='lightExp', max_length=255)),
                ('lightexpinfo', models.TextField(db_column='lightExpInfo')),
                ('humidity', models.CharField(max_length=255)),
                ('humidinfo', models.CharField(db_column='humidInfo', max_length=255)),
                ('humidexp', models.CharField(db_column='humidExp', max_length=255)),
                ('humidexpinfo', models.TextField(db_column='humidExpInfo')),
                ('tempexp', models.CharField(db_column='tempExp', max_length=255)),
                ('tempexpinfo', models.TextField(db_column='tempExpInfo')),
            ],
            options={
                'db_table': 'plants',
                'managed': False,
            },
        ),
    ]
