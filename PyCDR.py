#!/usr/bin/python

import sys
import csv
import time
import re

"""
PyCDR.py

Author: Steve Campbell, Github: https://github.com/sdcampbell/PyCDR

Purpose: Searches the Cisco Call Manager (CUCM) Call Detail Records (CDR) csv file for an extension,
and saves the Date/Time, call duration, calling number, and called number to a new csv file.

Directions: Download the CDR from https://<cucmserver>/ccmservice/, select the date range,
and DO NOT CHECK 'CMR RECORDS'!
Run this script and specify three command line arguments:
1. The path and name of the input csv file
2. The path and name of the output csv file
3. The extension to search for

Example: PyCDR.py "/path/to/cdr.txt" "/path/to/output.txt" 4357
"""


def date_and_time(time_value):
    return time.strftime("%m/%d/%y %H:%M:%S", time.localtime(float(time_value)))

def convert_duration(secs):
    secs = int(secs)
    m, s = divmod(secs, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

if __name__ == '__main__':

    usage = 'Error, Correct Usage: PyCDR.py "/path/to/cdrfile" "/path/to/output.txt" 4357 "path/to/summary/out2.txt"'

    if (len(sys.argv) < 5):
        print(usage)
        sys.exit()

    else:
        infile = open((sys.argv[1]), 'r')
        outfile = open((sys.argv[2]), 'w')
#       Experimental out2 to add another output file summarizing TON calls.
        out2 = open((sys.argv[4]), 'w')
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
#        writer2 = csv.writer(out2)
#       Placehoder for International call counting
        IntCalls = 0
        NatCalls = 0

        writer.writerow(['Date/Time', 'Duration', 'Calling Number', 'Called Number', 'Final Called Number'] )


        for row in reader:
            if row[8] == (sys.argv[3]) or row[29] == (sys.argv[3]):
                writer.writerow([date_and_time(row[47]),convert_duration(row[55]),row[8],row[29], row[30]])
                matchInternat = re.match(r'\+[^1].+', row[8], re.M|re.I)
                matchNat = re.match(r'\+1*', row[8], re.M|re.I)
#                writer2.writerow("file")
                if matchInternat:
                   IntCalls += 1
                if matchNat:
                   NatCalls += 1



#        writer2.writeline(IntCalls)
        International = "International calls: %s" % IntCalls
        National = "National calls: %s" % NatCalls
        out2.write(International + "\n")
        out2.write(National + "\n")
        print("Finished successfully!")
        infile.close()
        outfile.close()
        out2.close()
