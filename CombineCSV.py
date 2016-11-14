#!/usr/bin/python

####################################
# Author: Carl Baccus
# This script is meant to combine files saved from CUCM CDR server that are more frequent (like every minute) and concatenate them together so they can be 
# processed by PyCDR and output to an XLS spreadsheet 
#concatenate all CSV's together but clean header row first.
####################################

import glob
import re

interesting_files = glob.glob("cdr*") 

header_saved = False
with open('output.csv','wb') as fout:
    for filename in interesting_files:
        print filename
        with open(filename) as fin:
        	for line in fin:
        		if re.match(".+cdrRecordType.+",line):
					pass
        		elif re.match(".+VARCHAR.+", line):
					pass
			else:
        			fout.write(line)
 
