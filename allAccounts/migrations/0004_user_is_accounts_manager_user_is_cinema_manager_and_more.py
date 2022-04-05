# Generated by Django 4.0.2 on 2022-03-30 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allAccounts', '0003_remove_user_is_accounts_manager_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_accounts_manager',
            field=models.BooleanField(default=False, verbose_name='is_accounts_manager'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_cinema_manager',
            field=models.BooleanField(default=False, verbose_name='is_cinema_manager'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_clubRep',
            field=models.BooleanField(default=False, verbose_name='is_clubRep'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_student',
            field=models.BooleanField(default=False, verbose_name='is_student'),
        ),
    ]