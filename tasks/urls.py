from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from django.urls import path
from .views import TaskViewSet, TaskDetailAPIView, TaskUpdateAPIView, TaskDeleteAPIView

# router = DefaultRouter()
# router.register(r'tasks', TaskViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]


# tasks/urls.py


urlpatterns = [
    path('tasks/', TaskViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='task-list'),
    path('tasks/<int:id>/', TaskDetailAPIView.as_view(), name='task-detail'),
    path('tasks/<int:id>/update/', TaskUpdateAPIView.as_view(), name='task-update'),
    path('tasks/<int:id>/delete/', TaskDeleteAPIView.as_view(), name='task-delete'),
]
