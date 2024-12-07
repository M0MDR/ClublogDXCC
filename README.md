By Martin M0MDR / DL3RDR

This little project queries www.clublog.org for the DXCC entity of a given callsign.

Please see "Release" for a Windows executable.

Usage:
ClublogDXCC [-D YYYYMMDD] callsign
If a date is provided it shows the DXCC of the given date. When no date is provided, today's date is used.

Limitations:
Clublog's date checking does not seem very strict. If an invalid date is provided (e.g. 20240230) the query defaults to today's date.

FURTHER READING

The method used to query Clublog is described here:
https://clublog.freshdesk.com/support/solutions/articles/54904-how-to-query-club-log-for-dxcc-info

If you want to run the Python code or use it in your own project you need to put a valid API Key in the file "ClublogAPIKey.py" (see file "ClublogAPIKey.demo.py" for the format). The way to request a free API key is described here:
https://clublog.freshdesk.com/support/solutions/articles/54910-api-keys
