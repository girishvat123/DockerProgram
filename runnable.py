#!/usr/local/bin/python

import csv
import json
import os
import datetime
import sys
# Figure out the current time of the snapshot
# Checking if it is append or write operation
if not (len(sys.argv) == 3):
        print("Arguments: Specify the OUTPUT CSV FILE"),
        sys.exit(1),

mode=""
currentTime=datetime.datetime.now().timestamp()
opFile=str(sys.argv[1])
rootPath= str(sys.argv[2])
jsonFile={}
headers=['TimeStamp','TenantID','Metric','Value']

if os.path.exists(opFile):
    mode="a"
else:
    mode="w"

outputFile= open(opFile,mode)
# go through all folders and find the json files and folder name
for subdirs,files,subfiles in os.walk(rootPath):
    for content in subfiles:
        if content.endswith(".json"):

            subdirSplit=subdirs.split("/")
            path= os.path.join(subdirs,content);
            tenantId=subdirSplit[-1]
            if tenantId not in jsonFile:
                jsonFile[tenantId]=path
            
writer=csv.DictWriter(outputFile, delimiter=',', lineterminator='\n',fieldnames=headers)

# when it is write mode , we write the headers for the first time

if mode is 'w':
    writer.writeheader()
#Loop through each Json file and write its value into CSV file
for folder,data in jsonFile.items():
    currentJsonFile=open(data)
    jsonValues=json.load(currentJsonFile)
     
    for metric, value in jsonValues.items():
        writer.writerow({'TimeStamp':currentTime,'TenantID':folder,"Metric":metric,"Value":value})
	
outputFile.close()
