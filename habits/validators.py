from datetime import timedelta

from rest_framework import serializers


class FieldCompatibilityValidator:
    """Валидация на невозможность одновременного заполнения полей 'related_habit' и 'reward'"""

    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, habit):
        if habit.get('related_habit') and habit.get('reward'):
            raise serializers.ValidationError(
                'Нельзя одновременно указывать связанную привычку и вознаграждение'
            )


class DurationValidator:
    """Валидация поля 'duration' на то, что оно не превышает 120 секунд"""

    def __init__(self, field_1):
        self.field_1 = field_1

    def __call__(self, habit):
        if habit.get('duration') > timedelta(seconds=120):
            raise serializers.ValidationError(
                'Время выполнения не должно превышать 120 секунд'
            )


class RelatedIsNotPleasurableValidator:
    """Валидация поля 'related_habit' на то, что привычка является приятной"""

    def __init__(self, field_1):
        self.field_1 = field_1

    def __call__(self, habit):
        if habit.get('related_habit'):
            if habit.get('related_habit').is_pleasurable is False:
                raise serializers.ValidationError(
                    'Связанной привычкой может быть только приятная привычка'
                )


class NotRewardNotRelatedValidator:
    """Валидация на то, что у приятной привычки не может быть вознаграждения или связанной привычки"""
    def __init__(self, field_1, field_2, field_3):
        self.field_1 = field_1
        self.field_2 = field_2
        self.field_3 = field_3

    def __call__(self, habit):
        if habit.get('is_pleasurable') is True:
            if habit.get('related_habit') or habit.get('reward'):
                raise serializers.ValidationError(
                    'У приятной привычки не может быть вознаграждения или связанной привычки'
                )


class DaysOfWeekValidator:
    """Валидация на то, что привычка выполняется минимум раз в неделю"""

    def __init__(self, field_1):
        self.field_1 = field_1

    def __call__(self, habit):
        if habit.get('daysofweek'):
            days = habit.get('daysofweek')
            days_of_week = [
                days.get('monday'), days.get('tuesday'), days.get('wednesday'),
                days.get('thursday'), days.get('friday'), days.get('saturday'), days.get('sunday')
            ]

            if not any(days_of_week):
                raise serializers.ValidationError(
                    'Привычку нельзя выполнять реже одного раза в неделю'
                )
