# Generated by Django 4.0.2 on 2022-04-21 10:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UWE', '0012_ticket_movie_alter_movies_dateandtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='dateAndTime',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 21, 11, 8, 7, 24784)),
        ),
        migrations.AlterField(
            model_name='movies',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
