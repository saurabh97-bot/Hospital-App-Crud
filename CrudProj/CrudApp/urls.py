
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('create',patient_create),
    path('list',patient_list),
    path('update/<int:pk>',update_patient),
    path('delete/<int:pk>',delete_patient),
    path('logout',user_logout),
    path('login',user_login)
]