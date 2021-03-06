from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    PRN = models.CharField('Permanent Registration Number',
                           max_length=10, unique=True, blank=False)
    year = models.IntegerField('year studying ex: 1 - first year',
                               choices=[(1, 1), (2, 2), (3, 3), (4, 4)], blank=False, default=1)
    branch = models.CharField("branch currently studying", max_length=50, blank=False, choices=[
                              ("COMP", "COMP"), ("E&TC", "E&TC"), ("MECH", "MECH")], default="COMP")
    division = models.CharField("division currently studying", max_length=50, blank=False, choices=[
                                ("A", "A"), ("B", "B"), ("SS", "SS")])
    date_joined = models.DateTimeField(
        "date user created account", default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',
                       'PRN', 'year', 'branch', 'division']

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email
