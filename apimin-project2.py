# import requests
# city = input("Enter city:")
# url=f"http://wttr.in/{city}?format=j1"
# response = requests.get(url)
# data=response.json()
# temp=data["current_condition"][0]["temp_C"]
# print("Temperature:",temp,"C")
# humidity=data["current_condition"][0]["humidity"]
# print("Humidity:",humidity,"%")
# condition=data["current_condition"][0]["weatherDesc"][0]["value"]
# print("weather:",condition)
# windspeed=data["current_condition"][0]["windspeedKmph"]
# print("Wind speed:",windspeed,"km/h")

import requests
city = input("Enter city:")
url=f"http://wttr.in/{city}?format=j1"
response = requests.get(url)
data=response.json()
current=data["current_condition"][0]
print("\n----------Current Weather----------")
print("City:",city)
print("Temperature:",current["temp_C"],"C")
print("Humidity:",current["humidity"],"%")
print("Weather:",current["weatherDesc"][0]["value"])
print("Wind Speed:",current["windspeedKmph"],"km/h")
print("\n----------Weather Forecast----------")
hourly=data["weather"][0]["hourly"]
for hour in hourly:
    print(
        f"Time: {hour['time']} | "
        f"Temp: {hour['tempC']}C | "
        f"Humidity: {hour['humidity']}% | "
        f"Weather: {hour['weatherDesc'][0]['value']}"
    )