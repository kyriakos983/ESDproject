# Generated by Django 4.0.2 on 2022-03-28 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UWE', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='image',
            field=models.ImageField(blank=True, default=False, null=True, upload_to=''),
        ),
    ]