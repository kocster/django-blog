# Generated by Django 2.2.7 on 2019-12-15 20:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20191215_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 15, 20, 14, 10, 393643, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
