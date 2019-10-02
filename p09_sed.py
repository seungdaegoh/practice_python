#! /home/peter/anaconda3/bin/python3
#! /usr/bin/python3

import argparse
import os
import sys
import glob

parser = argparse.ArgumentParser(prog='sed.py', description='stream editor for filtering and transforming text' )
parser.add_argument('-e', '--expression' , metavar="script", type=str,
		help='add the script to the commands to be executed')

parser.add_argument('file', metavar='FILE', type=str, nargs='*' )	

args = parser.parse_args()

script = args.expression

print('script = ', script)
param = script.split('/')

print('param = ', param)


if (param[0] == 's') :

	as_is = param[1]
	to_be = param[2]

	fname =  args.file
	print( "args.file = ", fname )

	if (fname and fname[0]) :
		f = open(fname[0], 'r')
		in_method = f.readlines()
		f.close

	else :
		in_method = sys.stdin

	for line in in_method:
		if ( "\n"  not in line ) :
			print ("____end of input___")
			break

		
		changed = line.replace(as_is, to_be)

		print(changed, end='')
	
print('End of program')


