from django.db import models


class Student(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    student_name = models.CharField(max_length=50, null=True)
    student_email = models.EmailField(max_length=100, null=True)


class ClubRep(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    clubRep_name = models.CharField(max_length=30)
    club_rep_number = models.CharField(max_length=11)
    club_rep_email = models.EmailField(max_length=100, null=True)


class CinemaManager(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)


class Club(models.Model):
    club_name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200)
    postCode = models.CharField(max_length=10)
    house_num = models.IntegerField()
    city = models.CharField(max_length=50)
    phone_num = models.IntegerField()
    email = models.EmailField(max_length=100)


class screenChoices(models.TextChoices):
    screen1 = 'screen1'
    screen2 = 'screen2'
    screen3 = 'screen3'


class Movies(models.Model):
    name = models.CharField(max_length=50)
    screen = models.CharField(max_length=50, choices=screenChoices.choices, null=True, blank=True)
    dateAndTime = models.DateTimeField()
    ticketPrice = models.IntegerField()
    image = models.ImageField(null=True, blank=True)


class TicketDiscount(models.Model):
    name = models.CharField('Ticket type', max_length=50)
    price = models.PositiveIntegerField('Ticket price')

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
