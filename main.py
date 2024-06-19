import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 23.034160
MY_LONG = 72.548490


MY_EMAIL = "sbxp1966@gmail.com"
MY_PASS = "gogatmuwcjufqlet"


def postion_check():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def day_night_check():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrisesunset.io/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_12hf = (data["results"]["sunrise"])
    sunset_12hf = (data["results"]["sunset"])

    def convert24(str1):
        meridian = str1[-2:]
        time_part = str1[:-2].strip()
        hours, minutes, seconds = time_part.split(':')
        
        if meridian == "AM":
            if hours == "12":
                hours = "00"
        else:
            if hours != "12":
                hours = str(int(hours) + 12)
        
        return f"{hours.zfill(2)}:{minutes}:{seconds}"


    sunrise = int(convert24(sunrise_12hf).split(":")[0])
    sunset = int(convert24(sunset_12hf).split(":")[0])

    time_now = datetime.now()
    hour_now = time_now.hour


    if sunset <= hour_now and hour_now <= sunrise:
        return True


while True:
    time.sleep(300)
    if postion_check() and day_night_check():
        connection =  smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs= MY_EMAIL,
            msg=f"Subject:  Look Up Now! The ISS is in Your Sky! \n\n Look up now! The International Space Station is soaring across your sky!  Don't miss this incredible sight! "
        )

    else:
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs= MY_EMAIL,
            msg=f"Subject:  Program Running \n\n Program Running Fine"
        )