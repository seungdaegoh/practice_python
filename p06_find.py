#! /home/peter/anaconda3/bin/python3
#! /usr/bin/python3

import argparse

parser = argparse.ArgumentParser(prog='find', description='find files' )
parser.add_argument('dir',  type=str, nargs='+')
parser.add_argument('-name',  metavar='dir name', type=str)
parser.add_argument('-print',  action="store_true")

args = parser.parse_args()

# print( "args.dir = ", args.dir[0] )
# print( "args.name = ", args.name)


# print(type(args.dir[0]))
# print(type(args.name))

full_name = args.dir[0] + args.name

# print(full_name)


import glob
flist = glob.glob(full_name)

#print(flist)


for fname in flist:

	print(fname)

	if args.print :
		print(" print file's contents -------------")

		f = open(fname, 'r')
		lines = f.readlines()

		for line in lines:
			print(line, end = '')

		f.close()



# print('End of program')
