from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from .managers import User1Manager
# Create your models here.


class User1(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email_address'), unique=True)
    is_test1 = models.BooleanField(default=False)
    is_test2 = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = User1Manager()

    def __str__(self):
        return self.email

    def set_test_type(self, numb):
        if numb == 1:
            self.is_test1 = True
        elif numb == 2:
            self.is_test2 = True
        else:
            self.is_active = False
        self.save()
        
    def test_type(self):
        if self.is_test1:
            return 1
        elif self.is_test2:
            return 2
        else:
            return -1
