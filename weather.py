#!/usr/bin/python3

import requests
import xml.etree.ElementTree as ET
from datetime import datetime
from dateutil import parser
import geocoder

# a = geocoder.osm("Linköping")
latlng = geocoder.ip("me").latlng
print(latlng)

url = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={}&lon={}".format(latlng[0], latlng[1])
print(url)
response = requests.get(url, headers={'User-Agent': "Weather app"})
print(response.content)

# redirected from search
if response.url != url:
    url = response.url
    #url = url.replace("/sted/", "/place/")
response = requests.get(url + "forecast_hour_by_hour.xml")

if response.status_code != 200:
    # print("server error")
    exit(1)
# print(response.text)
# print(response.url)
root = ET.fromstring(response.text)

items = root.iter("time")

cur_time = next(items)
#symbol = cur_time.find("symbol").get("name")
temp = cur_time.find("temperature").get("value")
#rain = cur_time.find("precipitation").get("value")
symbol = ""
rain = ""

print(temp + "° ", end='')

#rain_start = None
#if float(rain) > 0:
#    symbol = symbol + "("+rain+")"
#    rain_start = cur_time
#else:  # find start of rain
#    for item in items:
#        if float(item.find("precipitation").get("value")) > 1.0:
#            rain_start = item
#            break
#
#if rain_start is not None:
#    rain_end = cur_time
#    for item in items:
#        if float(item.find("precipitation").get("value")) > 1.0:
#            rain_end = item
#        else:
#            break
#
#    if rain_start is not cur_time or rain_end is not cur_time:
#        print(" ", end='')
#        
#    date_start = parser.parse(rain_start.get("from"))
#
#    if rain_start is not cur_time:
#        print(date_start.hour, "-", sep='', end='')
#    elif rain_end is not cur_time:
#        print("-", end='')
#
#    if rain_end is not None and rain_end is not cur_time:
#        date_end = parser.parse(rain_end.get("to"))
#        print(date_end.hour, end='')
#    elif rain_start is not None:
#        date_end = parser.parse(rain_start.get("to"))
#        print(date_end.hour, end='')
#
#    day_diff = abs(date_start.day - datetime.now().day)
#    if day_diff > 0:
#        print("(", day_diff, ")", sep='', end='')
#
#
print()
