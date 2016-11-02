#!/usr/bin/python
 
import sys
import csv
import time
import re
import xlsxwriter
from datetime import datetime
 
"""
PyCDR.py
 
Author: Carl Baccus
Special thanks to original work done by Steve Campbell.
This version is specifically catered to prepopulating an Excel spreadsheet.
This version in particular is used for a very purpose specific means.
"""
workbook = xlsxwriter.Workbook((sys.argv[2])+'.xlsx')
worksheet = workbook.add_worksheet()

# set formatting for date in excel
format1 = workbook.add_format({'num_format': 'mm/dd/yy hh:mm:ss'})
 
def date_and_time(time_value):
    return time.strftime("%m/%d/%y %H:%M:%S", time.localtime(float(time_value)))
 
def convert_duration(secs):
    secs = int(secs)
    m, s = divmod(secs, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

with open((sys.argv[1]), 'r') as infile:
    reader = csv.reader(infile)
    next(reader, None)  # skip the headers
    xrow = 0
    xcol = 0
    worksheet.write(xrow, xcol, "Date-time")
    worksheet.write(xrow, xcol + 1, "Duration")
    worksheet.write(xrow, xcol + 2, "Calling Number")
    worksheet.write(xrow, xcol + 3, "Called Number")
    worksheet.write(xrow, xcol + 4, "Final Called Number")
    worksheet.write(xrow, xcol + 5, "finalCalled-UserID")
    xrow = 1
    for row in reader:
        if row[47] == "0":
            pass
        elif re.match("\d+" + "5000", row[29]):
            worksheet.write(xrow, xcol, date_and_time(row[47]), format1)
            worksheet.write(xrow, xcol + 1, convert_duration(row[55]))
            worksheet.write(xrow, xcol + 2, row[8])
            worksheet.write(xrow, xcol + 3, row[29])
            worksheet.write(xrow, xcol + 4, row[30])
            worksheet.write(xrow, xcol + 5, row[31])
            xrow += 1
    print "All Done"
workbook.close()
