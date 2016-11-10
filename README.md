# PyCDR-Advanced

This script takes a Cisco UCM CDR file and parses it.  It is a fork of the original script written by Steve Campbell:
http://github.com/sdcampbell/PyCDR.py
I have modified it to include various other parameters within the CDR.
This script is also tested and working with version 10.5.2 of CUCM
No warranty is implied, USE AT YOUR OWN RISK!!!
This script is simply trying to fix some issues I have with reporting, and summarizing the extremely large data set from 
Cisco CDR's.

###Improvements completed 
* ~~added ability to do a search for pattern of a call in either Calling, Called, or FinalCalled.~~
* Reduced search pattern to Called Number only (more useable)
* Cleaned entire codebase to be a bit more effecient.
* added in a check to see if original CDR had Header row, and bypass if it does.
* Added if statement to exclude all zero second calls, and the datestamp that showed 0.
* Changed output file to write directly to Excel spreadsheet (this allows date format to be set, and phone numbers to be imported as text)

###Future enhancements planned
<<<<<<< HEAD
* This special branch is specifically to get the data imported directly into an excel spreadsheet so that pivot charts can be made
=======
* Add in usage directions
>>>>>>> 28326d60225ea46c00417966d228ec91a2d53d91
