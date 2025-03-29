from django.urls import path
from . views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('dashboard/', dashboard, name = 'dashboard'),
    path('register/', register, name = 'register'),
    path('login/', login, name = 'login'),
    path('logout/', logout, name = 'logout'),

    path('thought/create/', createThought, name = 'thought-create'),
    path('thoughts/<str:username>', myThoughts, name = 'thoughts-mine'),

]