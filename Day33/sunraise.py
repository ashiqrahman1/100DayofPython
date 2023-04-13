import requests
from datetime import datetime
MY_LAT = 17.114543
MY_LONG = 77.981774
parameter = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
response = requests.get(
    url="https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]
current = datetime.now()
print(current.hour)
print(f"{sunrise}")
