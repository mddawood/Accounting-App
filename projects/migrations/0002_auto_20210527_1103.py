# Generated by Django 3.1.7 on 2021-05-27 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='miscellaneous',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-start_date']},
        ),
    ]