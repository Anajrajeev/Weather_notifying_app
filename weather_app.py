import json
import time
import requests
while True:
    url="http://api.weatherapi.com/v1/forecast.json?key=api_key_here&q=bangalore&days=3"
    response=requests.get(url)
    data=response.json()
    #print(json.dumps(data, indent=4))
    temperature = data['current']['temp_c']
    humidity = data['current']['humidity']
    last_updated=data['current']['last_updated']
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Time:{last_updated}")
    if temperature > 25:
        print("Temprature exceeded average TOO HOT")
    if temperature < 18:
        print("Tempreture exceeded average TOO COLD")
    if humidity > 90:
        print("It's about to rain take shelter")
    with open('weather_data.csv', 'a') as file:
        file.write(f"{temperature}, {humidity},{last_updated}\n")
    time.sleep(3600)