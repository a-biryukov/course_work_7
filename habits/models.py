from datetime import timedelta

from django.db import models

from config.settings import AUTH_USER_MODEL, NULLABLE


class Habit(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Создатель привычки',
        **NULLABLE
    )
    action = models.CharField(
        max_length=100,
        verbose_name='Действие',
        help_text='Введите действие, которое представляет собой привычка'
    )
    place = models.CharField(
        max_length=100,
        verbose_name='Место выполнения привычки',
        help_text='Введите место, в котором неоходимо выполнять привычку'
    )
    duration = models.DurationField(
        default=timedelta(seconds=60),
        verbose_name='Время на выполнение привычки',
        help_text='Введите предположительное время, в течении которого будете выполнять привычку'
    )
    reward = models.CharField(
        max_length=254,
        verbose_name='Вознаграждение',
        help_text='Введите вознаграждение за выполнение привычки',
        **NULLABLE
    )
    related_habit = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        verbose_name='Связанная привычка',
        help_text='Укажите связанную привычку',
        **NULLABLE
    )
    is_pleasurable = models.BooleanField(
        default=False,
        verbose_name='Признак приятной привычки'
    )
    is_public = models.BooleanField(
        default=False,
        verbose_name='Признак публичности',
        help_text='Могут ли другие пользователи видеть эту привычку'
    )

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

    def __str__(self):
        return self.action


class DaysOfWeek(models.Model):
    habit = models.OneToOneField(
        Habit,
        on_delete=models.CASCADE,
        verbose_name='Привычка',
        **NULLABLE
    )
    monday = models.BooleanField(
        default=True,
        verbose_name='Понедельник'
    )
    tuesday = models.BooleanField(
        default=True,
        verbose_name='Вторник'
    )
    wednesday = models.BooleanField(
        default=True,
        verbose_name='Среда'
    )
    thursday = models.BooleanField(
        default=True,
        verbose_name='Четверг'
    )
    friday = models.BooleanField(
        default=True,
        verbose_name='Пятница'
    )
    saturday = models.BooleanField(
        default=True,
        verbose_name='Суббота'
    )
    sunday = models.BooleanField(
        default=True,
        verbose_name='Воскресенье'
    )

    class Meta:
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'

    def __str__(self):
        return (
            f'Понедельник - {self.monday}, '
            f'Вторник - {self.tuesday}, '
            f'Среда - {self.wednesday}, '
            f'Четверг - {self.thursday}, '
            f'Пятница - {self.friday}, '
            f'Суббота - {self.saturday}, '
            f'Воскресенье - {self.sunday}'
        )


class Runtime(models.Model):
    habit = models.OneToOneField(
        Habit,
        on_delete=models.CASCADE,
        verbose_name='Привычка',
        **NULLABLE
    )
    time_1 = models.TimeField(
        verbose_name='Время выполнения привычки',
        help_text='Введите время, когда нужно выполнять привычку'
    )
    time_2 = models.TimeField(
        verbose_name='Время выполнения привычки',
        help_text='Введите время, когда нужно выполнять привычку',
        **NULLABLE
    )
    time_3 = models.TimeField(
        verbose_name='Время выполнения привычки',
        help_text='Введите время, когда нужно выполнять привычку',
        **NULLABLE
    )
    time_4 = models.TimeField(
        verbose_name='Время выполнения привычки',
        help_text='Введите время, когда нужно выполнять привычку',
        **NULLABLE
    )
    time_5 = models.TimeField(
        verbose_name='Время выполнения привычки',
        help_text='Введите время, когда нужно выполнять привычку',
        **NULLABLE
    )

    class Meta:
        verbose_name = 'Время выполнения'
        verbose_name_plural = 'Время выполнения'

    def __str__(self):
        return (
            f'1. {self.time_1}, '
            f'2. {self.time_2}, ' 
            f'3. {self.time_3}, ' 
            f'4. {self.time_4}, ' 
            f'5. {self.time_5}'
        )
