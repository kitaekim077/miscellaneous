#!usr/bin/python
import sys

input_file  = sys.argv[1]
output_file = sys.argv[2]

FH = open(input_file,"r")
FW = open(output_file,"w")

for sLine in FH.readlines():
	#sLine = sLine.strip()
	if sLine[0] != '>':
		sLine = sLine.upper()
		FW.write(sLine)
	else:
		FW.write(sLine)

FH.close()
FW.close()
