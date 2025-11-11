import requests
from datetime import datetime as dt

MY_LAT = 11.733816
MY_LNG = 78.962578

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
time_now = dt.now()

print(sunrise)
print(sunset)
print(time_now.hour)

