# Generated by Django 3.1.7 on 2021-05-27 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'ordering': ['-date']},
        ),
    ]