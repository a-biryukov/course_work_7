from rest_framework import viewsets, generics

from habits.models import Habit
from habits.paginators import CustomPaginator
from habits.permissions import IsOwner
from habits.serializer import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = CustomPaginator

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ['retrieve', 'update', 'destroy', 'partial_update']:
            self.permission_classes = [IsOwner]

        return super().get_permissions()

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset.filter(user=self.request.user).order_by('id')


class PublicHabitsListAPIView(generics.ListAPIView):
    queryset = Habit.objects.filter(is_public=True).order_by('id')
    serializer_class = HabitSerializer
    pagination_class = CustomPaginator
