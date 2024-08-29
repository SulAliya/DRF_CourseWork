from rest_framework.viewsets import ModelViewSet

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.serializer import HabitSerializer
from habits.services import create_periodic_task
from users.permissions import IsModer, IsOwner


class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator

    # def perform_create(self, serializer):
    #     habit = serializer.save()
    #     habit.user = self.request.user
    #     habit.save()
    #
    #     hour = habit.time.hour
    #     minute = habit.time.minute
    #     # week_list = [0 - Monday, 1 - Tuesday, 2 - Wednesday, 3 - Thursday, 4 - Friday, 5 - Saturday, 6 - Sunday]
    #     week_list = []
    #     if habit.monday:
    #         week_list.append(0)
    #     if habit.tuesday:
    #         week_list.append(1)
    #     if habit.wednesday:
    #         week_list.append(2)
    #     if habit.thursday:
    #         week_list.append(3)
    #     if habit.friday:
    #         week_list.append(4)
    #     if habit.saturday:
    #         week_list.append(5)
    #     if habit.sunday:
    #         week_list.append(6)
    #
    #     print(f'{hour}:{minute}, {week_list}')
    #     message = f'{habit.action} в {habit.place} в {habit.time}'
    #     print(f'{message} to {self.request.user.tg_chat_id}')
    #
    #     create_periodic_task(self.request.user.username, habit.pk, hour, minute, week_list, message,
    #                          self.request.user.tg_chat_id)

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (~IsModer,)
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = (IsModer | IsOwner,)
        elif self.action == 'destroy':
            self.permission_classes = (~IsModer | IsOwner,)

        return super().get_permissions()
