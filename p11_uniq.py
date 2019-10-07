#! /home/peter/anaconda3/bin/python3
#! /usr/bin/python3

import argparse
import sys

parser = argparse.ArgumentParser(prog='uniq.py',
		description='Filter adjacent matching lines from INPUT (or standard input)' )
args = parser.parse_args()

in_method = sys.stdin

ulist = [];

for line in in_method:
	if ( "\n"  not in line ) :
		print ("____end of input___")
		break


	if (line not in ulist) :
		#print("same : ", line);
		#else :
		ulist.append(line)

#print(ulist)

for it in ulist:
	print(it, end='')

#print('End of program')



