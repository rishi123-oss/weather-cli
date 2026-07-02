import requests
import sys
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    

    if data["cod"] != 200:
        print(f"Error: {data['message']}")
        return

    print(f"City: {data['name']}")
    print(f"Temp: {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description']}")

city = sys.argv[1]
get_weather(city)   