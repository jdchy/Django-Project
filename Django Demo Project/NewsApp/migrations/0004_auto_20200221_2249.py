# Generated by Django 3.0.2 on 2020-02-21 16:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0003_news_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 2, 21, 16, 49, 13, 300761, tzinfo=utc)),
        ),
    ]
