import os
from dotenv import load_dotenv
import requests
load_dotenv("weatherkey.env")

city=input("======== Weather ========\nEnter city name:\n")
api_key= os.getenv("API_KEY")
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
     
