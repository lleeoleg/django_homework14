from django.urls import path, re_path
from app import views

urlpatterns = [
    # Обычные маршруты
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/add/', views.task_add, name='task_add'),
    
    re_path(r'^tasks/(?P<task_id>\d+)/$', views.task_detail, name='task_detail'),
    re_path(r'^tasks/(?P<task_id>\d+)/update/$', views.task_update, name='task_update'),
    re_path(r'^tasks/(?P<task_id>\d+)/delete/$', views.task_delete, name='task_delete'),
]
