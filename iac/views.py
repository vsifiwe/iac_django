from rest_framework.views import APIView
from rest_framework.response import Response
from .helpers import Helpers

class DataView(APIView):

    def get(self, request, format=None):
        origin, destination = Helpers().get_locations()
        distance, duration = Helpers().get_distance_duration(origin, destination)
        print(distance, duration)
        return Response({"message": "Hello World!"})

class EventsView(APIView):
    def get(self, request, format=None):
        email = request.GET.get('email')
        events = Helpers().get_events(email)
        return Response({"message": events})

class SwitchView(APIView):
    def get(self, request, format=None):
        type = request.GET.get('type')

        if type == 'on':
            return Response({"message": "We turned on the alarm"})

        if type == 'off':
            return Response({"message": "We turned off the alarm"})

class TestView(APIView):
    def get(self, request, format=None):
        w = Helpers().get_earliest_event_time('asifiwemanzi@gmail.com')
        return Response({"message": w})