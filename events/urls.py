from django.urls import path
from . import views

urlpatterns = [
    path('<str:id>/', views.event, name="event"),
    path('register/<str:id>/', views.event_register, name="event_register"),
]
