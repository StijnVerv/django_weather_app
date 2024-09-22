
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import json
import os

# Construct the path to config.json
config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config.json')

# Load the configuration file
with open(config_path) as config_file:
    config = json.load(config_file)

# Access the API key
api_key = config['openWeatherApiKey']

@api_view(['GET'])
def get_weather(request):
    city = request.GET.get('city')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
        }
        return Response(weather_data)
    else:
        return Response({'error': 'City not found'}, status=404)

# Create your views here.
