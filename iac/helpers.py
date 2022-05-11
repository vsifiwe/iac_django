import os
import googlemaps
import requests
import json
import dateutil.parser
from datetime import timedelta

class Helpers:
    def get_distance_duration(self, origin, destination):
        key = os.getenv("APIKEY")
        gmaps = googlemaps.Client(key=key)
        results = gmaps.distance_matrix(origins=origin, destinations=destination, arrival_time=1652334335, mode="driving")
        # returns (distance, duration)
        return results['rows'][0]['elements'][0]['distance']['text'], results['rows'][0]['elements'][0]['duration']['text']


    def get_locations(self):
        # returns (origin, destination)
        return (-1.9634, 30.1349), (-1.9438, 30.0596)
    
    def get_events(self, email):
        r = requests.get('https://iac-backend.herokuapp.com/events?email='+email)
        results = json.loads(r.content)
        if 'events' in results:
            return results['events']
        else:
            return []

    def get_earliest_event_time(self, email):
        events = self.get_events(email)

        if len(events) == 0:
            return 0
            
        tm = dateutil.parser.isoparse(events[0]['start']['dateTime'])
        tm = tm + timedelta(hours=2)
        time = tm.timestamp()
        return int(time)

    def get_weather(self):
        key = os.getenv("WEATHER")
        url = "http://api.weatherapi.com/v1/forecast.json?q=-1.9441,30.0619&key=" + key + "&days=3"

        r = requests.get(url)
        result = json.loads(r.content)
        chance = result['forecast']['forecastday'][1]['day']['daily_chance_of_rain']
        if chance > 50:
            return True
        return False

    def calculate_everything(self):
        origin, destination = self.get_locations()
        _ , duration = self.get_distance_duration(origin, destination)
        print("we are calculating")