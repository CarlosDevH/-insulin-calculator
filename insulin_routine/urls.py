from django.urls import path
from . import views

urlpatterns = [
    path('new_routine/', views.create_insulin_routine, name='create_insulin_routine'),
]