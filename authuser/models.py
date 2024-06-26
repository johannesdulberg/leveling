from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', unique=True)
    name = models.CharField(max_length=255, blank=True, default='')

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    favorites = models.ManyToManyField(
        'moves.Exercise', blank=True, related_name='favorited')
    learned = models.ManyToManyField(
        'moves.Exercise', blank=True, related_name='learned')
    want_to_learn = models.ManyToManyField(
        'moves.Exercise', blank=True, related_name='want_to_learn')
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()
    PROGRESS_CHOICES = (
        (0, 'Never Tried'),
        (10, 'Tried in Lines'),
        (20, 'In Lines (5 seconds+)'),
        (30, 'With Spotters (5 s+)'),
        (40, 'In Lines (10 s+)'),
        (50, 'With Spotters (10 s+)'),
        (60, 'Out of Lines (10 s+)'),
        (70, 'Consistently Out of Lines with Multiple People (10 s+)'),
        (80, 'Consistently Out of Lines No Steps (10 s+)'),
        (90, 'Consistently Out of Lines No Steps with Multiple People (10 s+)'),
        (100, 'Mastered')
    )
    

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name or self.email.split('@')[0]

