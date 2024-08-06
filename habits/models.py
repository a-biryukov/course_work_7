from django.db import models

from config.settings import AUTH_USER_MODEL, NULLABLE


class Habit(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name='Создатель привычки',
        on_delete=models.CASCADE,
        **NULLABLE
    )
    place = models.CharField(
        max_length=100,
        verbose_name='Место выполнения привычки',
        help_text='Введите место, в котором неоходимо выполнять привычку'
    )
    time = models.TimeField(
        verbose_name='Время выполнения привычки',
        help_text='Введите время, когда нужно выполнять привычку'
    )
    action = models.CharField(
        max_length=100,
        verbose_name='Действие',
        help_text='Введите действие, которое представляет собой привычка'
    )
    periodicity = models.CharField(
        max_length=100,
        verbose_name='Периодичность выполнения привычки',
        help_text='Введите периодичность выполнения привычки',
        default='Ежедневно'
    )
    pleasurable_habit = models.BooleanField(
        verbose_name='Признак приятной привычки'
    )
    related_habit = models.CharField(
        max_length=100,
        verbose_name='Связанная привычка',
        **NULLABLE
    )
    reward = models.CharField(
        max_length=254,
        verbose_name='Вознаграждение',
        help_text='Введите вознаграждение за выполнение привычки',
        **NULLABLE
    )
    time_doing = models.CharField(
        max_length=100,
        verbose_name='Время на выполнение привычки',
        help_text='Введите предположительное время, в течении которого будете выполнять привычку'
    )
    publicity = models.BooleanField(
        verbose_name='Публичная привычка',
        help_text='Могут ли другие пользователи видеть вашу привычку?'
    )

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

    def __str__(self):
        return self.action

