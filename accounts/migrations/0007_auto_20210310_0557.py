# Generated by Django 3.1.7 on 2021-03-10 00:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210310_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 10, 0, 27, 44, 199781, tzinfo=utc)),
        ),
    ]
