# PyCDR-Advanced

This script takes a Cisco UCM CDR file and parses it.  It is a fork of the original script written by Steve Campbell:
http://github.com/sdcampbell/PyCDR.py
I have modified it to include various other parameters within the CDR.
This script is also tested and working with version 10.5.2 of CUCM
No warranty is implied, USE AT YOUR OWN RISK!!!
This script is simply trying to fix some issues I have with reporting, and summarizing the extremely large data set from 
Cisco CDR's.

###Improvements being worked on
* add another file that summaraized number of calls to specific TON's (IE: International, National, Subscriber)
* Summarize hours:minutes:seconds from duration for a given extension
* Summarize how many calls rolled to voicemail unnaswered.
