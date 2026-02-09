import requests
from dotenv import load_dotenv
import os


load_dotenv()


def get_weather(city: str):
    API_KEY=os.getenv("OPENWEATHER_API_KEY")

    if not API_KEY:
        return "Weather service not configured."

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        r = requests.get(url, params=params, timeout=5)

        if r.status_code != 200:
            return f"Weather unavailable for {city}"

        data = r.json()

        return {
            "city": city.title(),
            "description": data["weather"][0]["description"],
            "temp": data["main"]["temp"],
        }

    except Exception as e:
        return f"Error fetching weather: {str(e)}"
