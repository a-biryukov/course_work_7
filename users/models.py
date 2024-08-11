from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='Электронная почта',
        help_text='Введите электронную почту'
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name='Аватар',
        help_text='Загрузите фото',
        **NULLABLE
    )
    phone = models.CharField(
        max_length=35,
        verbose_name='Телефон',
        help_text='Введите номер телефона',
        **NULLABLE
    )
    country = models.CharField(
        max_length=100,
        verbose_name='Страна',
        help_text='Введите страну',
        **NULLABLE)
    chat_id = models.CharField(
        max_length=100,
        verbose_name='Телеграм chat-id',
        help_text='Введите телеграм chat-id',
        **NULLABLE
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
