from django.db import models
from django.contrib.auth.models import AbstractUser


# Identify which user is it
class User(AbstractUser):
    # Different users of the web application for login identification
    is_student = models.BooleanField('is_student', default=False)
    is_clubRep = models.BooleanField('is_clubRep', default=False)
    is_cinema_manager = models.BooleanField('is_admin', default=False)
    is_accounts_manager = models.BooleanField('is_accounts_manager', default=False)

