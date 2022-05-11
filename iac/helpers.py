import os
import googlemaps

class Distance:
    def get_distance_duration(self, origin, destination):
        key = os.getenv("APIKEY")
        gmaps = googlemaps.Client(key=key)
        results = gmaps.distance_matrix(origins=origin, destinations=destination, arrival_time=1652334335, mode="driving")
        # returns (distance, duration)
        return results['rows'][0]['elements'][0]['distance']['text'], results['rows'][0]['elements'][0]['duration']['text']


    def get_locations(self):
        # returns (origin, destination)
        return (-1.9634, 30.1349), (-1.9438, 30.0596)


class Events:
    def get_events(self, email):
        return []