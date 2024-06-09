import requests

# Function to fetch weather data from OpenWeatherMap API
def fetch_weather_data(location, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

# Function to display weather information
def display_weather_info(data):
    if data["cod"] != 200:
        print("Error:", data["message"])
    else:
        print(f"Weather in {data['name']}, {data['sys']['country']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather Conditions: {data['weather'][0]['description']}")

# Main function
def main():
    api_key = "9761be57143a399184e0fc5992c60a2d"  # Replace with your OpenWeatherMap API key
    location = input("Enter city name or ZIP code: ")
    
    # Fetch weather data
    weather_data = fetch_weather_data(location, api_key)
    
    # Display weather information
    display_weather_info(weather_data)

if __name__ == "__main__":
    main()
