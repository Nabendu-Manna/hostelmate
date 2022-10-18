from django.urls import path

from hostelmate import settings
from .views import RoomPostView, RoomPostDetailsView

urlpatterns = [
    path('room/', RoomPostView.as_view()),
    path('room/<int:pk>', RoomPostDetailsView.as_view()),
]