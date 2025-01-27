# Generated by Django 5.0.7 on 2024-08-06 16:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(help_text='Введите действие, которое представляет собой привычка', max_length=100, verbose_name='Действие')),
                ('place', models.CharField(help_text='Введите место, в котором неоходимо выполнять привычку', max_length=100, verbose_name='Место выполнения привычки')),
                ('time_doing', models.DurationField(help_text='Введите предположительное время, в течении которого будете выполнять привычку', verbose_name='Время на выполнение привычки')),
                ('periodicity', models.CharField(choices=[('Несколько раз в день', 'Несколько раз в день'), ('Ежедневно', 'Ежедневно'), ('В определенные дни недели', 'В определенные дни недели')], default='Ежедневно', help_text='Введите периодичность выполнения привычки', verbose_name='Периодичность выполнения привычки')),
                ('reward', models.CharField(blank=True, help_text='Введите вознаграждение за выполнение привычки', max_length=254, null=True, verbose_name='Вознаграждение')),
                ('publicity', models.BooleanField(help_text='Могут ли другие пользователи видеть вашу привычку?', verbose_name='Публичная привычка')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель привычки')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
        migrations.CreateModel(
            name='DaysOfWeek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.BooleanField(default=True, verbose_name='Понедельник')),
                ('tuesday', models.BooleanField(default=True, verbose_name='Вторник')),
                ('wednesday', models.BooleanField(default=True, verbose_name='Среда')),
                ('thursday', models.BooleanField(default=True, verbose_name='Четверг')),
                ('friday', models.BooleanField(default=True, verbose_name='Пятница')),
                ('saturday', models.BooleanField(default=True, verbose_name='Суббота')),
                ('sunday', models.BooleanField(default=True, verbose_name='Воскресенье')),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habits.habit', verbose_name='Привычка')),
            ],
            options={
                'verbose_name': 'День недели',
                'verbose_name_plural': 'Дни недели',
            },
        ),
        migrations.CreateModel(
            name='RelatedHabit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(help_text='Укажите действие, которое представляет собой привычка', max_length=100, verbose_name='Действие')),
                ('is_pleasurable', models.BooleanField(verbose_name='Признак приятной привычки')),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habits.habit', verbose_name='Полезная привычка')),
            ],
            options={
                'verbose_name': 'Связанная привычка',
                'verbose_name_plural': 'Связанные привычки',
            },
        ),
        migrations.CreateModel(
            name='Runtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_1', models.TimeField(help_text='Введите время, когда нужно выполнять привычку', verbose_name='Время выполнения привычки')),
                ('time_2', models.TimeField(blank=True, help_text='Введите время, когда нужно выполнять привычку', null=True, verbose_name='Время выполнения привычки')),
                ('time_3', models.TimeField(blank=True, help_text='Введите время, когда нужно выполнять привычку', null=True, verbose_name='Время выполнения привычки')),
                ('time_4', models.TimeField(blank=True, help_text='Введите время, когда нужно выполнять привычку', null=True, verbose_name='Время выполнения привычки')),
                ('time_5', models.TimeField(blank=True, help_text='Введите время, когда нужно выполнять привычку', null=True, verbose_name='Время выполнения привычки')),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habits.habit', verbose_name='Привычка')),
            ],
            options={
                'verbose_name': 'Время выполнения',
                'verbose_name_plural': 'Время выполнения',
            },
        ),
    ]
