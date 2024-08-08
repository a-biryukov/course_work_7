from django.urls import path
from rest_framework.routers import SimpleRouter

from habits.apps import HabitsConfig
from habits.views import HabitViewSet, HabitListAPIView

app_name = HabitsConfig.name

router = SimpleRouter()
router.register('', HabitViewSet)

urlpatterns = [
    path('list/', HabitListAPIView.as_view(), name='habit_list')
] + router.urls
