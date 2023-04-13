import requests
from datetime import datetime
import smtplib
import time
MY_LAT = 20.593683  # Your latitude
MY_LONG = 78.962883  # Your longitude


def iss_issoverhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(f"ISS Latitude {iss_latitude} longitude {iss_longitude}")
    # Your position is within +5 or -5 degrees of the ISS position.

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # print(f"My Sunrise: {sunrise} Sunset: {sunset}")
    time_now = datetime.now()
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True


while True:
    time.sleep(60)
    if iss_issoverhead and is_night():
        with smtplib.SMTP('smtp.gmail.com') as con:
            con.starttls()
            con.login(user="testusername@gmail,com", password="testpassword")
            con.sendmail(to_addrs="totest1@gmail.com",
                         from_addr="testusername@gmail.com")
# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
