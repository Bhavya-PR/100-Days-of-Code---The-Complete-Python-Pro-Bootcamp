import requests
from datetime import datetime as dt
import smtplib
import time

MY_LAT = 11.733816
MY_LNG = 78.962578
MY_MAIL = "tester.python.course@gmail.com"
MY_PASSWORD = "rurs kcib ovkl jlpo"

# ISS Position API

def iss_overhead():
    response_iss_position = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss_position.raise_for_status()
    data_iss_position = response_iss_position.json()
    longitude = float(data_iss_position['iss_position']['longitude'])
    latitude = float(data_iss_position['iss_position']['latitude'])
    iss_position = (longitude,latitude)
    if MY_LNG-5 <= longitude <= MY_LNG+5 and MY_LAT-5 <= latitude <= MY_LAT+5:
        return True
    return False

# Sunrise and Sunset API

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }
    response_sunrise_sunset = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response_sunrise_sunset.raise_for_status()
    data_sunrise_sunset = response_sunrise_sunset.json()
    sunrise = int(data_sunrise_sunset["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_sunrise_sunset["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = dt.now()
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True
    return False

while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_MAIL,password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_MAIL,
                to_addrs=MY_MAIL,
                msg="Subject:Look Up\n\nThe ISS is above you in the sky"
            )


