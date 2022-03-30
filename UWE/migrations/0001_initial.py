# Generated by Django 4.0.2 on 2022-03-30 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CinemaManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=200)),
                ('postCode', models.CharField(max_length=10)),
                ('house_num', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('phone_num', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ClubRep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('clubRep_name', models.CharField(max_length=30)),
                ('club_rep_number', models.CharField(max_length=11)),
                ('club_rep_email', models.EmailField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('screen', models.CharField(blank=True, choices=[('screen1', 'Screen1'), ('screen2', 'Screen2'), ('screen3', 'Screen3')], max_length=50, null=True)),
                ('dateAndTime', models.DateTimeField()),
                ('ticketPrice', models.IntegerField()),
                ('tickets', models.IntegerField(default=300)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('student_name', models.CharField(max_length=50, null=True)),
                ('student_email', models.EmailField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TicketDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField(default=False)),
                ('sale_price', models.IntegerField(default=False)),
                ('new_price', models.IntegerField(default=False)),
            ],
        ),
    ]
