from django.db import models
from django.contrib.auth.models import AbstractUser

ADMIN = 'admin'
MODERATOR = 'moderator'
USER = 'user'

CHOICES = (
    (ADMIN, ADMIN),
    (MODERATOR, MODERATOR),
    (USER, USER),
)

class User(AbstractUser):
    email = models.EmailField(
        max_length=254,
        unique=True,
    )
    role = models.CharField(
        max_length=10,
        choices=CHOICES,
        default=USER,
        verbose_name='Роль пользователя',
    )
    bio = models.TextField(blank=True, verbose_name='Биография')
    confirmation_code = models.CharField(
        max_length=100,
        verbose_name='Токен пользователя',
    )
    def __str__(self):
        return '%s' % (self.username)

    class Meta:
        verbose_name = ('Пользователь')
        verbose_name_plural = ('Пользователи')
        ordering = ('id',)
