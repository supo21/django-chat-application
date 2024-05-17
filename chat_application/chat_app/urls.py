from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_rooms, name="all_rooms"),
    path("<str:slug>/", views.room, name="room"),
]