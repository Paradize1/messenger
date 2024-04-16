from django.urls import path

from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('rooms/<id>', views.room, name='room'),
    path('room_create/', views.create_room, name='room_create'),
    path('send_message/', views.send_message, name='send_message'),

]