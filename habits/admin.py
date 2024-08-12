from django.contrib import admin

from habits import models


@admin.register(models.Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'action', 'place', 'duration',
        'reward', 'related_habit', 'is_pleasurable', 'is_public',
    )


@admin.register(models.DaysOfWeek)
class DaysOfWeekAdmin(admin.ModelAdmin):
    list_display = ('id', 'habit', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday',)


@admin.register(models.Runtime)
class RuntimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'habit', 'time_1', 'time_2', 'time_3', 'time_4', 'time_5',)
