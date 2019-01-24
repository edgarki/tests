#!/bin/python

import sys
import os
import urllib2
import json

from datetime import datetime


# Complete the function below.

def openAndClosePrices(firstDate, lastDate, weekDay):
    firstDate = datetime.strptime(firstDate, '%d-%B-%Y')
    lastDate = datetime.strptime(lastDate, '%d-%B-%Y')

    url = 'https://jsonmock.hackerrank.com/api/stocks/?page='
    page = 1
    d = getJSONURL(url+str(page))

    week = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}

    #data = []

    while page < d['total_pages'] + 1:
        #print page
        for i in range(d["per_page"]):
            dt = datetime.strptime(d["data"][i]["date"], '%d-%B-%Y')
            if firstDate <= dt and lastDate >= dt:
                w = datetime.strptime(d["data"][i]["date"], '%d-%B-%Y').weekday()
                if w == week[weekDay]:
                    #data.append([d["data"][i]["date"],d["data"][i]["open"],d["data"][i]["close"]])
                    print d["data"][i]["date"],d["data"][i]["open"],d["data"][i]["close"]
        page+=1
        d = getJSONURL(url + str(page))



def getJSONURL(url):
    r = urllib2.Request
    try:
        r = urllib2.urlopen(url)
        return json.loads(r.read())
    except IOError, e:
        return "Connection failed"




try:
    _firstDate = raw_input()
except:
    _firstDate = None

try:
    _lastDate = raw_input()
except:
    _lastDate = None

try:
    _weekDay = raw_input()
except:
    _weekDay = None

openAndClosePrices(_firstDate, _lastDate, _weekDay)

# 21-January-2019 22-February-2000 Monday
# 1-January-2000 22-February-2000 Monday
