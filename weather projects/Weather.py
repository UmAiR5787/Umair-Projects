import os
from getpass import getpass
from pathlib import Path

from dotenv import load_dotenv
import requests

env_path = Path(__file__).with_name("weatherkey.env")
load_dotenv(env_path)

city=input("======== Weather ========\nEnter city name:\n")
api_key = os.getenv("API_KEY")
if not api_key:
   print("First-time setup: enter your API key below; it will not be displayed.")
   api_key = getpass("OpenWeather API key: ")
   if api_key:
      env_path.write_text(f"API_KEY={api_key}\n", encoding="utf-8")
if not api_key:
   raise RuntimeError("An OpenWeather API key is required.")
url1=f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
url2=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
op=input("===== Enter option =====\n (1 for current)\n (2. for week's forecast ) \n ")
if op == "1":
 response=requests.get(url2)
 if response.status_code == 200:
    data=response.json()
    Temp = data["main"]["temp"]
    Humidity = data["main"]["humidity"]
    Desc = data["weather"][0]["description"]
    print(f"""======== Weather for {city.title()}  ========\n Temperatue: {Temp}°C \n Humidity: {Humidity}% \n condition: {Desc.title()} \n""")
 else:
    print("The city name is not valid or the API key is isn't valid !")
elif op=="2":
  response1=requests.get(url1)
  if response1.status_code == 200:
    data=response1.json()
    forecast_list = data["list"]
    for item in forecast_list[:25]:
     time = item["dt_txt"]
     temp = item["main"]["temp"]
     desc = item["weather"][0]["description"]
     print(f"Time: {time} | Temp: {temp}°C | Condition: {desc}")
  else:
    print("The city name is invalid or the Api key is invalid!!")
     
