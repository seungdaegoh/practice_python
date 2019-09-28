#! /home/peter/anaconda3/bin/python3
#! /usr/bin/python3

import argparse

parser = argparse.ArgumentParser(prog='find', description='find files' )
parser.add_argument('dir',  metavar='N', type=str, nargs='+')
parser.add_argument('-name',  metavar='N', type=str, nargs='+')
parser.add_argument('-print',  metavar='N', type=str, nargs='+')

args = parser.parse_args()

	print( "args.file = ", args.file )



import glob
print(glob.glob("/home/adam/*.txt")

print('End of program')
