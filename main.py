import requests
from datetime import datetime
import smtplib
MY_LAT = 23.037451
MY_LONG = 72.563980

MY_EMAIL = "sbxp1966@gmail.com"
MY_PASS = "gogatmuwcjufqlet"


def postion_check():  
    if iss_latitude >= MY_LAT-5 and iss_latitude <= MY_LAT+5 and iss_longitude >= MY_LONG-5 and iss_longitude <= MY_LONG+5:
        return True
    else:
        return False
    
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

def day_night_check():
    if sunset <= hour_now and hour_now <= sunrise:
        return True
    else:
        return False


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

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

sunrise = int(convert24(sunrise_12hf).split(":")[0])
sunset = int(convert24(sunset_12hf).split(":")[0])

time_now = datetime.now()
hour_now = time_now.hour

# # -- Check Time if Day or Night
# print(f"Sunrise: {sunrise}")
# print(f"Sunset: {sunset}")
# print(f"Hour Now: {hour_now}")
# if sunset <= hour_now and hour_now <= sunrise:
#     print("Raat Bhai")
# else:
#     print("Din Bhai")



if postion_check == True and day_night_check == True:
    print("In the Sky")
#     with smtplib.SMTP("smtp.gmail.com") as smtp:
#         smtp.starttls()
#         smtp.login(user=MY_EMAIL, password=MY_PASS)
#         smtp.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs= MY_EMAIL,
#             msg=f"Subject:  Look Up Now! The ISS is in Your Sky! \n\n Look up now! The International Space Station is soaring across your sky!  Don't miss this incredible sight! "
#         )
#     print("Email Sent")

else:
    print("Not in the Sky")
#     with smtplib.SMTP("smtp.gmail.com") as smtp:
#         smtp.starttls()
#         smtp.login(user=MY_EMAIL, password=MY_PASS)
#         smtp.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs= MY_EMAIL,
#             msg=f"Subject: ISS Update: Not in the Sky Right Now \n\nHey there!\nJust a quick heads-up: The International Space Station is not visible in your sky at the moment. Keep an eye out for future opportunities to spot it! \nClear skies!\n"
#         )



