# Generated by Django 4.0.2 on 2022-03-30 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allAccounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='accountOptions',
            field=models.CharField(blank=True, choices=[('is_student', 'Is Student'), ('is_clubRep', 'Is Clubrep'), ('is_cinema_manager', 'Is Cinema Manager'), ('is_accounts_manager', 'Is Accounts Manager')], default=None, max_length=50, null=True),
        ),
    ]
