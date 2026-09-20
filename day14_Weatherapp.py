import requests

city = "Toronto"
response = requests.get("https://geocoding-api.open-meteo.com/v1/search", params={"name": city})
print(response.url)
data = response.json()
print(data)


print("--- Testing the specific search format ---")
response = requests.get("https://geocoding-api.open-meteo.com/v1/search", params={"name": "Toronto, Canada"})
data = response.json()
print(len(data["results"]))
print(data["results"][0]["name"], data["results"][0]["country"])
print(data)