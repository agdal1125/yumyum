# Generated by Django 3.2.6 on 2021-08-14 16:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matjip', '0003_auto_20210502_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 15, 1, 28, 7, 316744)),
        ),
        migrations.AlterField(
            model_name='place',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 15, 1, 28, 7, 316744)),
        ),
    ]
