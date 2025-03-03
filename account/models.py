import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models


PHONE_REGEX = RegexValidator(
    regex=r"^\+998([0-9][0-9]|99)\d{7}$",
    message="Please provide a valid phone number",
)

class UserManager(BaseUserManager):
    def create_user(self, phone_number, last_name, name, email, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('User must have a phone number')
        if not name:
            raise ValueError('User must have a name')
        if not last_name:
            raise ValueError('User must have a last name')
        if not email:
            raise ValueError('User must have an email')

        email = self.normalize_email(email)
        user = self.model(
            phone_number=phone_number,
            name=name,
            last_name=last_name,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, name, last_name, email, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone_number, last_name, name, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.CharField(validators=[PHONE_REGEX], max_length=21, unique=True, default="+998931112233")
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='accounts/photos/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)

    @property
    def is_doctor_status(self):
        return self.is_doctor

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name', 'email', 'last_name']

    def __str__(self):
        return f'{self.name} {self.last_name}'

    @property
    def is_staff(self):
        return self.is_admin