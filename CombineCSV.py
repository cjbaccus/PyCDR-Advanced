#!/usr/bin/python

######
# concatenate all CSV's together but clean header row first.
######

import glob
import re

interesting_files = glob.glob("cdr*") 

header_saved = False
with open('output.csv','wb') as fout:
    for filename in interesting_files:
        print filename




        with open(filename) as fin:
        	for line in fin:
        		if re.match("cdrRecordType.+",line):
					pass
        		else:
        			#print line
        			fout.write(line)
        		
        #    header = next(fin)
        #    if not header_saved:
        #        fout.write(header)
        #        header_saved = True
        #    for line in fin:
        #        fout.write(line)