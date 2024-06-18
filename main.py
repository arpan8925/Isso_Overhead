import requests
from datetime import datetime

MY_LAT = 23.037451 # Your latitude
MY_LONG = 72.563980 # Your longitude

def postion_check():  
    if iss_latitude >= MY_LAT-5 and iss_latitude <= MY_LAT+5 and iss_longitude >= MY_LONG-5 and iss_longitude <= MY_LONG+5:
        return True
    else:
        return False

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

postion_check()

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


time_now = datetime.now()
hour_now = time_now.hour



if sunset <= hour_now and hour_now >= sunrise:
    print("Raat Bhai")
else:
    print("Din Bhai")



# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



