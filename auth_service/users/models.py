from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import UserManager


class User(PermissionsMixin, AbstractBaseUser):

    username = models.CharField(unique=True, max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True, max_length=255)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    register_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self):
        return self.email

    def __repr__(self):
        return f"#{self.id}-{self.email}"

    @property
    def is_customer(self):
        return not self.is_superuser and not self.is_staff

    def serializer(self):
        return vars(self)
