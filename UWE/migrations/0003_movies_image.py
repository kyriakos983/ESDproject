# Generated by Django 4.0.2 on 2022-04-01 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UWE', '0002_alter_movies_tickets'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
