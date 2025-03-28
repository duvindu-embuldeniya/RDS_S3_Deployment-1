from django.urls import path
from . views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('register/', register, name = 'register'),
    path('login/', login, name = 'login'),
    path('logout/', logout, name = 'logout'),
    path('task/<int:pk>/', singleTask, name = 'task-detail'),
    path('task/create', createTask, name = 'task-create'),
    path('task/<int:pk>/update/', updateTask, name = 'task-update'),
    path('task/<int:pk>/delete/', deleteTask, name = 'task-delete'),
]