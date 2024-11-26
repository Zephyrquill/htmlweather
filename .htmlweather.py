import requests
import folium
from folium import Icon, Popup
import datetime

weather_descriptions = {
    "clear sky": "Clear sky",
    "few clouds": "Few clouds",
    "scattered clouds": "Scattered clouds",
    "broken clouds": "Broken clouds",
    "overcast clouds": "Overcast clouds",
    "light rain": "Light rain",
    "moderate rain": "Moderate rain",
    "heavy intensity rain": "Heavy intensity rain",
    "light snow": "Light snow",
    "snow": "Snow",
    "heavy snow": "Heavy snow",
    "light shower snow": "Light shower snow",
    "shower snow": "Shower snow",
    "heavy shower snow": "Heavy shower snow",
    "thunderstorm": "Thunderstorm",
    "thunderstorm with rain": "Thunderstorm with rain",
    "thunderstorm with heavy rain": "Thunderstorm with heavy rain",
    "thunderstorm with light rain": "Thunderstorm with light rain",
    "light intensity shower rain": "Light intensity shower rain",
}
#The data to the left of the : sign is API data.
#The ones on the right side are the ones that appear on the screen.
#So it is possible to make the ones on the right side the language you want.



info_list = []

cities = [
    {"name": "Tokyo", "latitude": 35.6762, "longitude": 139.6503},  # Japan
    {"name": "New York City", "latitude": 40.7128, "longitude": -74.0060},  # United States
    {"name": "London", "latitude": 51.5074, "longitude": -0.1278},  # United Kingdom
    {"name": "Paris", "latitude": 48.8566, "longitude": 2.3522},  # France
    {"name": "Berlin", "latitude": 52.5200, "longitude": 13.4050},  # Germany
    {"name": "Sydney", "latitude": -33.8688, "longitude": 151.2093},  # Australia
    {"name": "Dubai", "latitude": 25.276987, "longitude": 55.296249},  # United Arab Emirates
    {"name": "Singapore", "latitude": 1.3521, "longitude": 103.8198},  # Singapore
    {"name": "Los Angeles", "latitude": 34.0522, "longitude": -118.2437},  # United States
    {"name": "Barcelona", "latitude": 41.3784, "longitude": 2.1925},  # Spain
    {"name": "Rome", "latitude": 41.9028, "longitude": 12.4964},  # Italy
    {"name": "Amsterdam", "latitude": 52.3676, "longitude": 4.9041},  # Netherlands
    {"name": "Vienna", "latitude": 48.2082, "longitude": 16.3738},  # Austria
    {"name": "Zurich", "latitude": 47.3784, "longitude": 8.5401},  # Switzerland
    {"name": "Hong Kong", "latitude": 22.3193, "longitude": 114.1694},  # China
    {"name": "Ankara", "latitude": 39.9334, "longitude": 32.8597}  # Turkey (Capital)
]
#This is the method required to add the desired locations.


def get_weather_data(api_key, latitude, longitude):
    base_url = "BASE URL"
    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def temperature_to_color(temperature):
    if temperature < -20:
        return 'white'
    elif temperature < -10:
        return 'blue'
    elif temperature < 0:
        return 'lightblue'
    elif temperature < 10:
        return 'green'
    elif temperature < 20:
        return 'darkgreen'
    elif temperature < 30:
        return 'orange'
    elif temperature < 45:
        return 'red'
    elif temperature <= 50:
        return 'purple'
    elif temperature <= 55:
        return 'black'
    else:
        return 'black'

def main():

    api_key = "API KEY"
    
    map_all_cities = folium.Map(location=[38.7333, 35.4961], zoom_start=7, control_scale=True) #map opening position
    folium.TileLayer('openstreetmap').add_to(map_all_cities)

    for city in cities:
        location_name = city["name"]
        latitude = city["latitude"]
        longitude = city["longitude"]

        weather_data = get_weather_data(api_key, latitude, longitude)

        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]
        wind_speed = weather_data["wind"]["speed"]

        warning_message1 = None
        warning_message = None
        warning_message2 = None

        if temperature > 30:
            warning_message = "High Temperature Warning"
            warning_color = "red"
        if temperature < 10:
            warning_message1 = "Low Temperature Warning"
            warning_color1 = "blue"
        if temperature <= 1:
            warning_message1 = "Low Temperature and Icing Hazard"
            warning_color1 = "blue"
        if wind_speed > 5.5:
            warning_message2 = "Severe Wind Warning"
            warning_color2 = "red"
        
        temperature_color = temperature_to_color(temperature)
        custom_icon = Icon(color=temperature_color, icon='info-sign')

        popup_content = f"""
            <div style="text-align: center;">
                <h2>{location_name}</h2>
                <p>Temperature: {temperature}°C</p>
                <p>Humidity: %{humidity}</p>
                <p>Status: {weather_descriptions.get(description.lower(), description)}</p>
                <p>Wind Speed: {wind_speed} m/s</p>
                <p>Date: {datetime.datetime.now().strftime('%d.%m.%Y %H:%M')}</p>
                {f"<p style='margin-top: 10px; font-weight: bold; text-align: center; color: {warning_color};'>{warning_message}</p>" if warning_message else ""}
                {f"<p style='margin-top: 10px; font-weight: bold; text-align: center; color: {warning_color1};'>{warning_message1}</p>" if warning_message1 else ""}
                {f"<p style='margin-top: 10px; font-weight: bold; text-align: center; color: {warning_color2};'>{warning_message2}</p>" if warning_message2 else ""}
            </div>
        </div>
        """
        #It is possible to make the temperature, humidity and similar things in the language you want.
                
        if warning_message:
            info_list.append(f"<li>{location_name} - {warning_message}</li>")

        if warning_message1:
            info_list.append(f"<li>{location_name} - {warning_message1}</li>")

        if warning_message2:
            info_list.append(f"<li>{location_name} - {warning_message2}</li>")

        marker = folium.Marker(
            [latitude, longitude],
            popup=Popup(popup_content, max_width=300),
            icon=custom_icon
        )

        marker.add_to(map_all_cities)

    map_all_cities.save("htmlweather.html")
    print("Ready")

if __name__ == "__main__":
    main()
