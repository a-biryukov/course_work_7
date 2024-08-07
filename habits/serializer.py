from rest_framework import serializers

from habits.models import Habit, DaysOfWeek, Runtime


class DaysOfWeekSerializer(serializers.ModelSerializer):

    class Meta:
        model = DaysOfWeek
        exclude = ('id', 'habit',)


class RuntimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Runtime
        exclude = ('id', 'habit',)


class HabitSerializer(serializers.ModelSerializer):
    runtime = RuntimeSerializer()
    days_of_week = DaysOfWeekSerializer(source='daysofweek')

    class Meta:
        model = Habit
        fields = '__all__'

    def create(self, validated_data):
        days_of_week_data = validated_data.pop('daysofweek')
        runtime_data = validated_data.pop('runtime')

        habit = Habit.objects.create(**validated_data)
        DaysOfWeek.objects.create(habit=habit, **days_of_week_data)
        Runtime.objects.create(habit=habit, **runtime_data)

        return habit

    def update(self, instance, validated_data):
        days_of_week_data = validated_data.pop('daysofweek')
        runtime_data = validated_data.pop('runtime')

        days_of_week = instance.daysofweek
        runtime = instance.runtime

        instance.action = validated_data.get('action', instance.action)
        instance.place = validated_data.get('place', instance.place)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.periodicity = validated_data.get('periodicity', instance.periodicity)
        instance.reward = validated_data.get('reward', instance.reward)
        instance.related_habit = validated_data.get('related_habit', instance.related_habit)
        instance.is_pleasurable = validated_data.get('is_pleasurable', instance.is_pleasurable)
        instance.is_public = validated_data.get('is_public', instance.is_public)
        instance.save()

        days_of_week.monday = days_of_week_data.get('monday', days_of_week.monday)
        days_of_week.tuesday = days_of_week_data.get('tuesday', days_of_week.tuesday)
        days_of_week.wednesday = days_of_week_data.get('wednesday', days_of_week.wednesday)
        days_of_week.thursday = days_of_week_data.get('thursday', days_of_week.thursday)
        days_of_week.friday = days_of_week_data.get('friday', days_of_week.friday)
        days_of_week.saturday = days_of_week_data.get('saturday', days_of_week.saturday)
        days_of_week.sunday = days_of_week_data.get('sunday', days_of_week.sunday)
        days_of_week.save()

        runtime.time_1 = runtime_data.get('time_1', runtime.time_1)
        runtime.time_2 = runtime_data.get('time_2', runtime.time_2)
        runtime.time_3 = runtime_data.get('time_3', runtime.time_3)
        runtime.time_4 = runtime_data.get('time_4', runtime.time_4)
        runtime.time_4 = runtime_data.get('time_5', runtime.time_5)
        runtime.save()

        return instance