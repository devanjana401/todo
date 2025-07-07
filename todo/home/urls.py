from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_task/', views.add_task, name='add_task'),
    path('mark_done/<int:task_id>/', views.mark_done, name='mark_done'), 
    path('mark_undone/<int:task_id>/', views.mark_undone, name='mark_undone'),
]