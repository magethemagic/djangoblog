from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('retrieve/', user_retrieve, name='retrieve'),
    path('center/', user_center, name='center'),
    path('reset/', views.reset_password, name='reset'),
]
