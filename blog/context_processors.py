from .weather_agent.tools import get_weather

def weather_context(request):
    city = request.GET.get("city")
    weather = get_weather(city) if city else None

    return {
        "weather": weather,
        "city": city
    }
