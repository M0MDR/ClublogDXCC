#
# ClubLog DXCC Query
#
# by Martin M0MDR / DL3RDR
#
# To compile the file you need to request your own API key from clublog
# See https://clublog.freshdesk.com/support/solutions/articles/54910-api-keys
# Place your API Key in a file called ClublogAPIKey.py in the same directory with following content
# ClubLogAPIKey = "YourAPIKeyGoesHere"
#

import json
import requests
import sys
from ClublogAPIKey import ClubLogAPIKey

PrintUsage = 0
ErrorMSG = ""
response = ""

if len(sys.argv) == 2: 
    DXCall=sys.argv[1]
    response = requests.get("https://clublog.org/dxcc?call="+DXCall+"&api="+ClubLogAPIKey+"&full=1")

elif len(sys.argv) == 4:
    DXCall=sys.argv[3]

    if sys.argv[1] == "-D":
        Date = sys.argv[2]
    else:
        ErrorMSG = "Unknown parameter "+sys.argv[1]

    if ErrorMSG == "":
        if len(Date) != 8:
            ErrorMSG = "Invalid date format"
        else:
            year = Date[0:4]
            month = Date[4:6]
            day = Date[6:8]

# Clublog is relied on for date validation
# Today's date will be given if the provided date is invalid.

            response = requests.get("https://clublog.org/dxcc?call="+DXCall+"&api="+ClubLogAPIKey+"&year="+year+"&month="+month+"&day="+day+"&hour=00&minute=01&full=1")

elif len(sys.argv) ==1:
    PrintUsage = 1

else:
    ErrorMSG = "Invalid parameters"

if response != "":
    if response.status_code != 200:
        ErrorMSG = "Clublog request failed ("+str(response.status_code)+")"
    else:
        data = response.json()

        if data.get("DXCC")==0:
            ErrorMSG = "Invalid callsign"
        else:
            print(f'DXCC: {data.get("Name")} ({data.get("DXCC")})')

if ErrorMSG != "":
    print(ErrorMSG)
    print("")
    PrintUsage = 1

if  PrintUsage == 1:
    print("Queries ClubLog for the DXXC entity of a callsign.")
    print("")
    print("usage: ClublogDXCC [-D YYYYMMDD] callsign")
    print("")
    print("Limitation: No strict date validation is applied. Invalid dates are likely to be mapped to today's date.")
    print("")
    
