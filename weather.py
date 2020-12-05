#!/usr/bin/python3

import requests
import geocoder
import json

# a = geocoder.osm("Linköping")
latlng = geocoder.ip("me").latlng

url = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={}&lon={}".format(latlng[0], latlng[1])

response = requests.get(url, headers={'User-Agent': "Weather app"})

if response.status_code != 200:
    # print("server error")
    exit(1)

json = json.loads(response.content)

temp = json['properties']['timeseries'][0]['data']['instant']['details']['air_temperature']
symbol = ""
rain = ""

print(str(int(temp)) + "° ", end='')
print()
