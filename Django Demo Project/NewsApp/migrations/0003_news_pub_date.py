# Generated by Django 3.0.2 on 2020-02-21 13:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0002_sportnews'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 2, 21, 13, 53, 56, 133511, tzinfo=utc)),
        ),
    ]
