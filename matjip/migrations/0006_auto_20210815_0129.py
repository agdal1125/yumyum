# Generated by Django 3.2.6 on 2021-08-14 16:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matjip', '0005_auto_20210815_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 15, 1, 29, 22, 483624)),
        ),
        migrations.AlterField(
            model_name='place',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 15, 1, 29, 22, 483624)),
        ),
    ]
