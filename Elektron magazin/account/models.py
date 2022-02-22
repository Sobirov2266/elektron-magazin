from django.db import models

from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    GENDER_CHOICE = (
        ('MALE', 'male'),
        ('FEMALE', 'female')
    )
    phone_number = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True, null=True)
    gender = models.CharField(max_length=10, null=True, choices=GENDER_CHOICE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=150, blank=True, null=True, unique=True)
    password = models.CharField(max_length=255)
    is_verifed = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'username']
