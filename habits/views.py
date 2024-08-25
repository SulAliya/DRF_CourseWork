from rest_framework.viewsets import ModelViewSet

from habits.models import Habit
from habits.serializer import HabitSerializer


class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
