# Generated by Django 2.2.17 on 2021-02-08 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0017_auto_20210208_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mail_alarm_time',
            field=models.TimeField(null=True),
        ),
    ]