#!/usr/bin/python
 
import sys
import csv
import time
import re
 
"""
PyCDR.py
 
Author: Carl Baccus
Special thanks to original work done by Steve Campbel
"""
 
 
def date_and_time(time_value):
    return time.strftime("%m/%d/%y %H:%M:%S", time.localtime(float(time_value)))
 
def convert_duration(secs):
    secs = int(secs)
    m, s = divmod(secs, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)
 
with open((sys.argv[1]), 'r') as infile, open((sys.argv[2]), 'w') as outfile:
    reader = csv.reader(infile)
    next(reader, None)  # skip the headers
    writer = csv.writer(outfile)
    writer.writerow(['Date/Time', 'Duration', 'Calling Number', 'Called Number', 'Final Called Number', 'finalCalledPartyUnicodeLoginUserID'] )
    for row in reader:
        if row[47] == "0":
            pass
        else:
            writer.writerow([date_and_time(row[47]),convert_duration(row[55]),row[8],row[29], row[30], row[31]])
    print "All Done"