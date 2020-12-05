#!/usr/bin/python3
import requests
import geocoder
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--location", help="Location (address) to get. Defaults to your IP address")
args = parser.parse_args()

if args.location is None:
    latlng = geocoder.ip("me").latlng
else:
    latlng = geocoder.osm(args.location).latlng

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
