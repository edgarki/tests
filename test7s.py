#!/usr/bin/python

# 7Shift - Vanhackaton Challenge
# @ Edgar K. Cintho
# date: 2018-06-23 17:12

import urllib2
import json
import datetime
import numpy

# download JSON
def getJson(url):
    req = urllib2.Request(url)
    opener = urllib2.build_opener()
    f = opener.open(req)
    data = json.loads(f.read())
    f.close()
    return data

# get Location JSON
def listLoc(url):
    loc = getJson(url).keys()
    return loc

# get users JSON
def listUsers(url,loc):
    usr = getJson(url)[loc].keys()
    return usr

# count and group hours per week
def clockP(url,usrID):
    clk = getJson(url)
    k = clk.keys()

    k = numpy.asarray(k)

    dict = {}

    # find all user id register in clockP
    dWeek = {}
    f = "%Y-%m-%d %H:%M:%S"
    for i in range(len(k)):


        if usrID == int(clk[k[i]]["userId"]):
            cOut = clk[k[i]]["clockedOut"]
            cIn = clk[k[i]]["clockedIn"]

            try:
                cOut = datetime.datetime.strptime(cOut, f)
                cIn = datetime.datetime.strptime(cIn, f)
                #print cIn.year
                #print cIn.month
                #print cIn.weekday()
                week = cIn.isocalendar()[1]
                hour = cOut - cIn

                try:
                    inc = hour + dWeek[week]
                except KeyError:
                    inc = hour
                hh = inc.seconds
                dWeek.update({ cIn.isocalendar()[1] : inc })

            except ValueError:
                break

    for i,j in dWeek.items() :
        ot = datetime.timedelta(seconds=3600 * 40)
        ot = j - ot
        dWeek.update({ i : ot })

    dict.update( { usrID : dWeek } )
    return dict

def checkAllEmployees(listUSR,cAEurl):
    cAE = {}
    for i in listUSR:
        clkURL = clockP(cAEurl, int(i))
        # need to fix output, now it's printing and return is disabled
        print clkURL
    #    cAE.update(clkURL)
    #return cAE


# variables and calling methods
locURL = "https://shiftstestapi.firebaseio.com/locations.json"

listLoc1 = listLoc(locURL)

usrURL = "https://shiftstestapi.firebaseio.com/users.json"

listUsr1 = listUsers(usrURL,listLoc1[0])

cAEurl = "https://shiftstestapi.firebaseio.com/timePunches.json"

checkAllEmployees(listUsr1,cAEurl)

