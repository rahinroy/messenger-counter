#%matplotlib inline

import json
import numpy as np
import matplotlib.pyplot as plt
import datetime
from dateutil import parser
import time 

#change for the all time graph comparision

#change name for the other graphs 
name = input("gib name")


#change based on what your name is 
yourName = "Edison Huang"

#change to max reply time (minutes)
minutes = 5

#dont change this it wont do anything lmfao
file = name.replace(" ", "")
file = file.lower()
file = file + "//"

#reply
replyMe =[]
replyOther =[]
avg = 0
f=0
#difference same
differenceOther =[]
differenceMe = []

#per hour
dayCounter= []
intDate = []
newDate = []
dayMessage = 0;
newDay = 0;
#general
stamp = []
messageCounter=[];
p = 0
objDate =[]
runonce = 0;
#time of day
otherTime=[]
meTime = []
timeDay = 0
count = 0
colored = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
title = ""


def startup(name):
    global p
    global messageCounter
    global newDay
    global dayCounter
    global objDate
    global stamp
    global timeDay
    global intDate
    global meTime
    global otherTime
    global replyMe
    global replyOther
    global differenceOther
    global differenceMe 
    global runonce
    global file
    global count
    global colored
    global title
    global minutes
    global newDate
    #dont change this it wont do anything lmfao
    file = name.replace(" ", "")
    file = file.lower()
    file = file + "//"

    #reply
    replyMe =[]
    replyOther =[]
    avg = 0
    f=0
    #difference same
    differenceOther =[]
    differenceMe = []

    #per hour
    dayCounter= []
    intDate = []
    newDate = []
    dayMessage = 0;
    newDay = 0;
    #general
    stamp = []
    messageCounter=[];
    p = 0
    objDate =[]
    runonce = 0;
    #time of day
    otherTime=[]
    meTime = []
    timeDay = 0
    people = []
    people.append(name)

    #dont change this it wont do anything lmfao

    with open(file + "message_1.json", encoding="utf8") as jFile:
        data = json.loads(jFile.read())
        for x in range(len(data["messages"])):
            stamp.append(data["messages"][p]["timestamp_ms"])
            messageCounter.append(p+1)
            objDate.append(datetime.datetime.fromtimestamp(stamp[p]/1000))
            intDate.append(stamp[p]/1000) 
        #time of messages
            if((data["messages"][p]["sender_name"]) == name):
                timeDay = (data["messages"][p]["timestamp_ms"]/1000)-21600
                timeDay = timeDay%86400
                timeDay = timeDay/3600
                otherTime.append(timeDay)
            if((data["messages"][p]["sender_name"]) == yourName):
                timeDay = (data["messages"][p]["timestamp_ms"]/1000)-21600
                timeDay = timeDay%86400
                timeDay = timeDay/3600
                meTime.append(timeDay)    

        #24 hrs
            if ((intDate[newDay]-intDate[p])>86400):
                dayMessage = messageCounter[p]-messageCounter[newDay]
                newDay = p
                newDate.append(datetime.datetime.fromtimestamp(stamp[p]/1000))
                dayCounter.append(dayMessage)
        #difference in reply
            #if (((intDate[p]-21600)%86400)>21600 or ((intDate[p]-21600)%86400)<7200): 
            if p>=1:
                if (((data["messages"][p-1]["sender_name"]) == name) and ((data["messages"][p]["sender_name"]) == yourName)):
                    if (((intDate[p-1]/60)-(intDate[p]/60))<minutes):
                        replyOther.append((intDate[p-1]/60)-(intDate[p]/60))
                if (((data["messages"][p]["sender_name"]) == name) and ((data["messages"][p-1]["sender_name"]) == yourName)):
                    if (((intDate[p-1]/60)-(intDate[p]/60))<minutes):
                        replyMe.append((intDate[p-1]/60)-(intDate[p]/60))
            p=p+1
    runonce = 1
    messageCounter = messageCounter[::-1]

def  doAll():
    global avg
    global f
    global count
    global restart
    global name
    fig, (timeGraphChart, perDayChart, timeOther, timeMe, replyOtherChart, replyMeChart) = plt.subplots(6, 1,num=None, figsize=(10, 25), dpi=80, facecolor='w', edgecolor='k')
    #fig.subplots(6,1, sharey=False )
    fig.subplots_adjust(hspace = 0.5)

    startup(name)
    #timeGraphChart = fig.add_subplot(1,1,1)
    timeGraphChart.plot(objDate, messageCounter)
    #timeGraphChart.figure(num=None, figsize=(10, 6), dpi=80, facecolor='w', edgecolor='k')
    timeGraphChart.margins(x=0, y=0)
    #plt.plot( objDate, messageCounter)
    timeGraphChart.set_title("name")

    #perDayChart = fig.add_subplot(2,1,2)
    perDayChart.bar(newDate, dayCounter)
    perDayChart.set_title(name + " per 24hrs")

    #timeOther
    timeOther.hist(otherTime, 144)
    timeOther.margins(x=0, y=0)
    timeOther.set_title("time of messages," + name)

    #timeMe = fig.add_subplot(4,1,4)
    timeMe.hist(otherTime, 144)
    timeMe.margins(x=0, y=0)
    timeMe.set_title("time of messages," + yourName)

    #replyOtherChart = fig.add_subplot(5,1,5)
    replyOtherChart.hist(replyOther, 144)
    replyOtherChart.margins(x=0, y=0)
    replyOtherChart.set_title("time to reply (minutes) , " + name)

    #replyMeChart = fig.add_subplot(6,1,6)
    replyMeChart.hist(replyMe, 144)
    replyMeChart.margins(x=0, y=0)
    replyMeChart.set_title("time to reply," + yourName + " , minutes ")

    
    f=0
    avg=0
    for x in range(len(replyMe)):
        avg = avg+replyMe[f]
        f = f+1
    print("edison avg reply: " + str(avg/len(replyMe)*60))

    f=0
    avg=0
    for x in range(len(replyOther)):
        replyOther[f]
        avg = avg+replyOther[f]
        f = f+1
    print(name +  " avg reply: " + str(avg/len(replyOther)*60))
    
    print ("number of messages of " + name + ": " + str(len(otherTime)))
    print ("number of messages of edison: " + str(len(meTime)))

    plt.show()

    restart = input("again: y/n")
    if (restart=="y"):
        name = input("name? ")
        f=0
        #plt.clf()
        doAll()

doAll()
