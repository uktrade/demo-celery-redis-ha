from django.urls import path
from .views import HomeView, TaskView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('task/<str:pk>/', TaskView.as_view(), name='task')
]
