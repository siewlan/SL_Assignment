#Assignment1 - Session16 (placeName with 10 days temp)
import requests
import json

#1) User to enter the placeName (can only access to city "medak")
placeName=input("Enter the city -> ")

#2) Build the url based on the input
url="http://api.openweathermap.org/data/2.5/forecast/daily?q=%s,in&cnt=10&mode=json&units=metric&APPID=2d80cf7142a085e6c34f383205d35118"%(placeName)

#3) Get the weather data (requests.models.Responses --> convert to str --> convert to dict)
weatherresp=requests.get(url)
weatherstr=weatherresp.text
weatherdict=json.loads(weatherstr)

#4) Display the 10 days temp - min, max, description
print("The url built is \n",url)
for eachEntry in weatherdict.get("list"):
	print("""
	Min Temp:%s\t Max Temp:%s\t Description:%s\t"""%(eachEntry.get('temp').get('min'),eachEntry.get('temp').get('min'),eachEntry.get('weather')[0].get('description')))
	