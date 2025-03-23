import requests

# Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
API_KEY = "YOUR_API_KEY"
CITY = "Tashkent"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

try:
    response = requests.get(URL)
    data = response.json()
    
    if response.status_code == 200:
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        
        print(f"Weather in {CITY}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_description.capitalize()}")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Error:", data.get("message", "Unable to fetch data"))

except Exception as e:
    print("An error occurred:", e)

