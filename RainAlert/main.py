import requests
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "f2f4540b039ffbb8aaff0ded00ad2f50"

weather_params = {
    'lat': 51.507351,
    'lon': -0.127758,
    'appid': api_key,
    'cnt': 4,
}

response = requests.get(OWM_endpoint, params=weather_params)
print(response.json())