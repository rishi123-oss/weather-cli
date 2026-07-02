# Weather CLI

A command-line tool that fetches real-time weather data for any city using the OpenWeatherMap API.

## Setup

1. Clone the repo
2. Install dependencies
   pip3 install requests python-dotenv
3. Get a free API key at openweathermap.org
4. Create a .env file and add:
   OPENWEATHERMAP_API_KEY=your_key_here

## Usage

python3 weather.py <city>

Example:
python3 weather.py London

## Output

City: London
Temp: 23.3°C
Weather: broken clouds

## Built With

- Python 3
- Requests library
- OpenWeatherMap API