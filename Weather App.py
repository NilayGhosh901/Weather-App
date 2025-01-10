import requests

# Replace with your OpenWeatherMap API key
API_KEY = "your_api_key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """
    Fetch weather data for a given city.
    
    :param city: Name of the city.
    :return: Weather details or an error message.
    """
    try:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'  # Use 'imperial' for Fahrenheit
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["cod"] == 200:
            weather = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"],
                "wind_speed": data["wind"]["speed"]
            }
            return weather
        else:
            return {"error": data["message"]}
    except Exception as e:
        return {"error": str(e)}

def display_weather():
    """
    Displays weather details for user-provided city.
    """
    city = input("Enter city name: ")
    weather = get_weather(city)
    if "error" in weather:
        print(f"Error: {weather['error']}")
    else:
        print(f"Weather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Description: {weather['description'].capitalize()}")
        print(f"Wind Speed: {weather['wind_speed']} m/s")

if __name__ == "__main__":
    display_weather()
