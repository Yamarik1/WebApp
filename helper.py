import re
import os
import json
import tkinter as tk

months = {'01': 31, '02': 29, '03':31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}

def read_data(years):
    data = {}
    currDate = ""
    path = os.path.join(os.getcwd(), "All Sessions")
    for filename in os.listdir(path):
        # print(filename)
        file_path = os.path.join(path, filename)
        with open(file_path, 'r') as file:
            content = file.read()
            currDict = json.loads(content)
            if currDict["startTime"][0:4] not in years:
                years.append(currDict["startTime"][0:4])
            # print(currDict["startTime"][0:10])
            if currDate != currDict["startTime"][0:10]:

                data[currDict["startTime"][0:10]] = []
                data[currDict["startTime"][0:10]].append(currDict)
                currDate = currDict["startTime"][0:10]
            else:
                data[currDict["startTime"][0:10]].append(currDict)
    # print(years)
    return data


# def parse_input(start, end):
#     datePattern = r"(0[0-9]|1[0-2])\-([1-2][0-9]|3[0-1])\-[\d]{4}"
#     # test1 = "12-25-1998"
#     # test2 = "NotValid"

#     startStr = start[0] + '-' + start[1] + '-' + start[2]
#     endStr = end[0] + '-' + end[1] + '-' + end[2]

#     if re.search(datePattern, startStr) == None:
#         return False
    
#     if re.search(datePattern, endStr) == None:
#         return False

#     if (int(start[1]) > months[start[0]]) or (int(end[1]) > months[end[0]]):
#         return False
    
#     #Check valid leap year
#     if (start[0] == '02' and start[1] == '29' and int(start[2]) % 4 != 0) or (end[0] == '02' and end[1] == '29' and int(end[2]) % 4 != 0):
#         return False


def clean_data(data, years):
    newData = {}
    for key, value in data.items():
        if len(value) == 1:
            newData[key] = value[0]

        else:
            baseDict = value.pop(0)

            for dict in value:
                baseDict.update(dict)
            newData[key] = baseDict

    return newData

def get_list(fullList, years):
    sublist = {}
    for key, val in fullList.items():
        if key[0:4] in years:
            sublist[key] = val
    return sublist
    # pass

# parse_input("s")

def get_insights(yearList):
    totalHeart = 0
    totalSteps = 0
    totalMiles = 0

    for key, value in yearList.items():

        for entry in value["aggregate"]:
            if entry["metricName"] == "com.google.heart_minutes.summary":
                totalHeart += entry["floatValue"]

            if entry["metricName"] == "com.google.step_count.delta":
                totalSteps += entry["intValue"]
            
            if entry["metricName"] == "com.google.distance.delta":
                totalMiles += entry["floatValue"]
            
    return [totalHeart, totalSteps, totalMiles]
    

def hide_frame(frame):
    frame.pack_forget()

def get_grid_list(yearList):
    gridList = []
    gridList.append(["Date", "Heart Points", "Steps", "Miles"])
    currIndex = 1
    for key, value in yearList.items():
        gridList.append([key, 0, 0, 0])

        for entry in value["aggregate"]:
            if entry["metricName"] == "com.google.heart_minutes.summary":
                gridList[currIndex][1] = entry["floatValue"]

            if entry["metricName"] == "com.google.step_count.delta":
                gridList[currIndex][2] = entry["intValue"]
            
            if entry["metricName"] == "com.google.distance.delta":
                gridList[currIndex][3] = entry["floatValue"] * .000621371

        currIndex += 1
    
    return gridList
            