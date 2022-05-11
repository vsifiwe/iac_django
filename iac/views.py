from rest_framework.views import APIView
from rest_framework.response import Response
from .helpers import Distance, Events

class DataView(APIView):

    def get(self, request, format=None):
        origin, destination = Distance().get_locations()
        distance, duration = Distance().get_distance_duration(origin, destination)
        print(distance, duration)
        return Response({"message": "Hello World!"})

class EventsView(APIView):
    def get(self, request, format=None):
        email = request.GET.get('email')
        events = Events().get_events(email)
        return Response({"message": events})