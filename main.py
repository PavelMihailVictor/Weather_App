


import requests



def get_weather(city):
    api_key = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if data["cod"] ==  200:
        weather = data["weather"][0]["description"]
        temperature = data ["main"]["temp"]
        temperature = round(temperature - 273.15, 2)
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        print(f"Weather in {city}:")
        print(f"Description: {weather}")
        print(f"Temperatur:{temperature}°C")
        print(f"Humidity:{humidity}%")
        print(f"Wind speed: {wind_speed} m/s")

    else:
        print("Failed to fetch weather data.")

def main():
    city = input("Enter you city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
