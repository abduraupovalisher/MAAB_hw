from bs4 import BeautifulSoup
import statistics

def parse_weather():
    with open("weather.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    
    weather_data = []
    rows = soup.find("table").find("tbody").find_all("tr")
    
    for row in rows:
        cols = row.find_all("td")
        day = cols[0].text
        temperature = int(cols[1].text.replace("°C", ""))
        condition = cols[2].text
        weather_data.append({"day": day, "temperature": temperature, "condition": condition})
    
    print("Weather Forecast:")
    for entry in weather_data:
        print(f"{entry['day']}: {entry['temperature']}°C, {entry['condition']}")
    
    max_temp = max(weather_data, key=lambda x: x['temperature'])
    sunny_days = [entry['day'] for entry in weather_data if entry['condition'] == "Sunny"]
    avg_temp = statistics.mean([entry['temperature'] for entry in weather_data])
    
    print(f"\nDay with the highest temperature: {max_temp['day']} ({max_temp['temperature']}°C)")
    print(f"Sunny days: {', '.join(sunny_days)}")
    print(f"Average temperature: {avg_temp:.2f}°C")

if __name__ == "__main__":
    parse_weather()

