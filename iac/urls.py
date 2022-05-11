from django.urls import path
from .views import DataView, EventsView

urlpatterns = [
    path('data', DataView.as_view()),
    path('events', EventsView.as_view())
]