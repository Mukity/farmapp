# Generated by Django 3.1.5 on 2021-02-18 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmapp', '0004_auto_20210218_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='Active',
        ),
    ]
