# Generated by Django 4.0.2 on 2022-04-21 10:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UWE', '0013_alter_movies_dateandtime_alter_movies_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='dateAndTime',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 21, 11, 15, 45, 459770)),
        ),
        migrations.AlterField(
            model_name='movies',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]
