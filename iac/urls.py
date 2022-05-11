from django.urls import path
from .views import DataView, EventsView, SwitchView, TestView

urlpatterns = [
    path('data', DataView.as_view()),
    path('events', EventsView.as_view()),
    path('switch', SwitchView.as_view()),
    path('test', TestView.as_view())
]