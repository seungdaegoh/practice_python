#! /home/peter/anaconda3/bin/python3
#! /usr/bin/python3

import argparse
import sys

parser = argparse.ArgumentParser(prog='sort.py',
		description='Write sorted concatenation of all FILE(s) to standard output.' )
parser.add_argument('-r', action='store_true', default=False,
	                    dest='reverse', help="reverse sort")

args = parser.parse_args()

in_method = sys.stdin
in_lines = [];

for line in in_method:
	if ( "\n"  not in line ) :
		print ("____end of input___")
		break

	in_lines.append(line)

#in_lines.sort();

if (args.reverse) :
	lines = sorted( in_lines, reverse=True)
else :
	lines = sorted( in_lines )

#print(in_lines);

for word in lines:
#print("  idx:", i, end=' ')
	print(word, end='')
#i += 1

#print('End of program')

