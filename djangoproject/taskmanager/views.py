from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend

from .permission import IsOwner
from .serializer import TaskViewSerializer, TaskDetailsSerializer, TaskLogsSerializer
from .models import Task


# Create your views here.
class TaskCreateView(generics.CreateAPIView):
    """
    This view create task for currently authenticated user.
    """
    serializer_class = TaskDetailsSerializer
    queryset = Task.objects.all()
    permission_classes = (IsOwner,)


class TaskDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    This view edit/view/del task
    for the currently authenticated user.
    """
    serializer_class = TaskDetailsSerializer
    queryset = Task.objects.all()
    permission_classes = (IsOwner,)


class TaskListView(generics.ListAPIView):
    """
    This view should return all tasks with or without filters
    for the currently authenticated user.
    """
    serializer_class = TaskViewSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['status', 'end_date']
    permission_classes = (IsOwner,)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskLogsView(generics.ListAPIView):
    serializer_class = TaskLogsSerializer
    permission_classes = (IsOwner,)
