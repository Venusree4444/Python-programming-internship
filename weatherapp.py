import requests

# OpenWeatherMap API key (Get your API key from OpenWeatherMap)
api_key = 'b73f861c9b47fe465e680a5d330e01eb'

# City for which you want to fetch weather data
city = 'Karimnagar'

# Base URL for the OpenWeatherMap API
base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

# Fetch current weather data
response = requests.get(base_url)
weather_data = response.json()

# Display current weather conditions
print(f"Current Weather in {city}:")
print(f"Weather: {weather_data['weather'][0]['description']}")
print(f"Temperature: {weather_data['main']['temp']}°C")
print(f"Humidity: {weather_data['main']['humidity']}%")
print(f"Wind Speed: {weather_data['wind']['speed']} m/s")

# Forecast URL for 5-day forecast
forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'

# Fetch 5-day forecast data
forecast_response = requests.get(forecast_url)
forecast_data = forecast_response.json()

# Display 5-day temperature trends
print("\n5-Day Temperature Trends:")
for forecast in forecast_data['list']:
    print(f"Date: {forecast['dt_txt']}, Temperature: {forecast['main']['temp']}°C")