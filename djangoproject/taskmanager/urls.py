from django.urls import path
from .views import TaskListView, TaskDetailsView, TaskCreateView, TaskLogsView

urlpatterns = [
    path('tasks/add/', TaskCreateView.as_view()),  # add task
    path('tasks/all/', TaskListView.as_view()),  # view all user tasks
    path('tasks/logs/<int:pk>/', TaskLogsView.as_view()),  # view task logs
    path('tasks/<int:pk>', TaskDetailsView.as_view()),  # view/edit/del task

]
