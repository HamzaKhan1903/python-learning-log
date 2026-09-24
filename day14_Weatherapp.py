import requests

'''city = "Toronto"
response = requests.get("https://geocoding-api.open-meteo.com/v1/search", params={"name": city})
print(response.url)
data = response.json()
print(data)


print("--- Testing the specific search format ---")
response = requests.get("https://geocoding-api.open-meteo.com/v1/search", params={"name": "Toronto, Canada"})
data = response.json()
print(len(data["results"]))
print(data["results"][0]["name"], data["results"][0]["country"])
print(data)'''

print("===============Weather App=================")
import requests
# API call 1 for getting the lat and long value of entered location
response = requests.get("https://geocoding-api.open-meteo.com/v1/search", params= {"name": "Toronto", "count": 5})
print(response.url)
geo = response.json()

#extracting clean results fo rthe put put that we need
clean_location = []
for location in geo["results"]:
    individual_location = {
        "name" : location["name"],
        "country": location["country"],
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "admin1": location["admin1"] 
    }
    clean_location.append(individual_location)

# Matches returned for and conditions to handle matches
number_of_results = len(clean_location)    
if number_of_results == 0:
    print("No mathcing location found. Please try again")

elif number_of_results == 1:
    selected_dict =clean_location[0]
    
else:
    for index, location in enumerate(clean_location):
        print(f"{index + 1}- {location['name']}, {location['admin1']}, {location['country']}")
    choice = int(input("Select the desired location"))
    selected_dict = clean_location[choice - 1]
    print(selected_dict)

URL = "https://api.open-meteo.com/v1/forecast"
parameter = {
	"latitude": selected_dict["latitude"],
	"longitude": selected_dict["longitude"],
	"current": ["temperature_2m", "apparent_temperature", "weather_code"],
	"timezone": "auto",
}

response = requests.get(URL, params= parameter)
print(response.status_code)
#print(response.json())
weather_conditions ={
	0: "Clear sky",
	1: "Mainly clear",
	2: "Partly cloudy",
	3: "Overcast",
	45: "Fog",
	48: "Depositing rime fog",
	51: "Light drizzle",
	53: "Moderate drizzle",
	55: "Dense drizzle",
	56: "Light freezing drizzle",
	57: "Dense freezing drizzle",
	61: "Slight rain",
	63: "Moderate rain",
	65: "Heavy rain",
	66: "Light freezing rain",
	67: "Heavy freezing rain",
	71: "Slight snowfall",
	73: "Moderate snowfall",
	75: "Heavy snowfall",
	77: "Snow grains",
	80: "Slight rain showers",
	81: "Moderate rain showers",
	82: "Violent rain showers",
	85: "Slight snow showers",
	86: "Heavy snow showers",
	95: "Thunderstorm",
	96: "Thunderstorm with slight hail",
	97: "Heavy thunderstorm",
	99: "Thunderstorm with heavy hail"
}
weather_response = response.json()
weather_clean ={
    "temp": weather_response["current"]["temperature_2m"],
    "feels_like": weather_response["current"]["apparent_temperature"],
    "condition": weather_conditions[weather_response["current"]["weather_code"]],
    "time": weather_response["current"]["time"]
}
print(
    f"For location: {selected_dict['name']}, "
    f"{selected_dict['admin1']}, {selected_dict['country']},\n"
    f"Current temperature: {weather_clean['temp']},\n"
    f"Feels like temperature: {weather_clean['feels_like']},\n"
    f"Current weather conditions: {weather_clean['condition']},\n"
    f"Time: {weather_clean['time']}"
)




