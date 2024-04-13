import requests
import json
import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

city = input("Enter the name of your city: \n")

url =f"https://api.weatherapi.com/v1/current.json?key=a5bdec50e1fb4406b33175943241004&q={city}"

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]


x = f"The current weather in {city} is {w} degrees."
speak.Speak(x)
print(x)