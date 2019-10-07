#! /usr/bin/python3
#! /home/peter/anaconda3/bin/python3

import argparse
import sys

parser = argparse.ArgumentParser(prog='sort.py',
		description='Write sorted concatenation of all FILE(s) to standard output.' )
parser.add_argument('-r', action='store_true', default=False,
	                    dest='reverse', help="reverse sort")

parser.add_argument('-f', '--ignore-case', action='store_true', default=False,
	                    dest='ignore_case', help="fold lower case to upper case characters")

parser.add_argument('-g', '--general-numeric-sort',  action='store_true', default=False,
	                    dest='num_sort', help="compare according to general numerical value")

args = parser.parse_args()


print("args.num_sort", args.num_sort, "args.ignore_case", args.ignore_case)

in_method = sys.stdin
in_lines = [];

for line in in_method:
    if ( "\n"  not in line ) :
        print ("____end of input___")
        break

    in_lines.append(line)

    if (args.num_sort):
        lines = sorted( in_lines, reverse=args.reverse, key=int)
    elif (args.ignore_case) :
        lines = sorted( in_lines, reverse=args.reverse, key=str.lower)
    else :
        lines = sorted( in_lines, reverse=args.reverse)

#print(in_lines);

for word in lines:
#print("  idx:", i, end=' ')
    print(word, end='')
#i += 1

#print('End of program')

