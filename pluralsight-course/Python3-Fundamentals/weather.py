import requests

url = 'http://api.weatherapi.com/v1/current.json?key=0dfaf1d3bf674562a3f22108240512&q=Ho chi minh&aqi=no'

response = requests.get(url)

weather_json = response.json()

temp_c = weather_json.get('current').get('temp_c')
description = weather_json.get('current').get('condition').get('text')


print("Today's weather in Ho Chi Minh city is", description, 'and', temp_c, 'degrees')
