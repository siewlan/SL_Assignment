#Assignment1 - Session16 (html response)
import requests
import json

#1) User to enter the placeName
placeName=input("Enter the city -> ")

#2) Build the url based on the input
url="http://api.openweathermap.org/data/2.5/weather?q=%s&mode=html&appid=d39b07db71b47cb0296ab70a2b84501b"%(placeName)

#3) Get the weather data
respObj=requests.get(url)
print(respObj)
respData=respObj.text
respData=respData.split('\n')

#remove <div style="display... to before </body>
#no. of values=36 i.e. 0 to 35
len(respData)
#index=27
respData.index('  <div style="display: block; clear: left; color: gray; font-size: x-small;">')
#remove index 27-33
respData.pop(33)
respData.pop(32)
respData.pop(31)
respData.pop(30)
respData.pop(29)
respData.pop(28)
respData.pop(27)

#convert python list to json object
data=json.dumps(respData)

#4) Display the data
print("The url built is \n",url)
print(respData)