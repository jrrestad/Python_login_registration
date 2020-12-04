from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_registration', views.registration),
    path('process_login', views.login),
    path('dashboard', views.dashboard),
]