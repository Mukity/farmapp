# Generated by Django 3.1.5 on 2021-02-20 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmapp', '0007_auto_20210220_0646'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Salary',
            field=models.IntegerField(default=7000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fertilizers',
            name='Price',
            field=models.IntegerField(default=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seedlings',
            name='Price',
            field=models.IntegerField(default=250),
            preserve_default=False,
        ),
    ]