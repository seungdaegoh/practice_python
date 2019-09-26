#! /home/peter/anaconda3/bin/python3
#! /usr/bin/python3

import argparse

parser = argparse.ArgumentParser(prog='PROG', description='print out file contents' )
parser.add_argument('file',  metavar='N', type=str, nargs='+')

args = parser.parse_args()

print( "args.file = ", args.file )

for fname in args.file :
	f = open(fname, 'r')
	lines = f.readlines()

	for line in lines:
		print(line, end = '')

	f.close()

# print("End of program")

