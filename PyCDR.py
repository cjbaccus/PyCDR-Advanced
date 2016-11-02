#!/usr/bin/python
 
import sys
import csv
import time
import re
import xlsxwriter
 
"""
PyCDR.py
 
Author: Carl Baccus
Special thanks to original work done by Steve Campbell
"""
workbook = xlsxwriter.Workbook('CDRdata.xlsx')
worksheet = workbook.add_worksheet()

 
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
    xrow = 0
    xcol = 0
    writer = csv.writer(outfile)
    writer.writerow(['Date/Time', 'Duration', 'Calling Number', 'Called Number', 'Final Called Number', 'finalCalled-UserID'] )
    # worksheet.write(A1, 'Date-Time', 'Duration', 'Calling Number', 'Called Number', 'Final Called Number', 'finalCalled-UserID')
    for row in reader:
        if row[47] == "0":
            pass
        elif re.match("\d+" + "5000", row[29]):
            # Just using 45000 for testing purposes.  Below worksheet lines will write each line into a column as it traverses row data.
            worksheet.write(xrow, xcol, date_and_time(row[47]))
            worksheet.write(xrow, xcol + 1, convert_duration(row[55]))
            worksheet.write(xrow, xcol + 2, row[8])
            worksheet.write(xrow, xcol + 3, row[29])
            worksheet.write(xrow, xcol + 4, row[30])
            worksheet.write(xrow, xcol + 5, row[31])
            xrow += 1
            writer.writerow([date_and_time(row[47]),convert_duration(row[55]),row[8],row[29], row[30], row[31]])
    print "All Done"
workbook.close()

"""
with open((sys.argv[1]), 'r') as infile, open((sys.argv[2]), 'w') as outfile:
    reader = csv.reader(infile)
    next(reader, None)  # skip the headers
    writer = csv.writer(outfile)
    writer.writerow(['Date/Time', 'Duration', 'Calling Number', 'Called Number', 'Final Called Number', 'finalCalled-UserID'] )
    for row in reader:
        if row[47] == "0":
            pass
        elif re.match("\d+"+(sys.argv[3]), row[8]) or re.match("\d+"+(sys.argv[3]), row[29]) or re.match("\d+"+(sys.argv[3]), row[30]):
            writer.writerow([date_and_time(row[47]),convert_duration(row[55]),row[8],row[29], row[30], row[31]])
    print "All Done"

"""