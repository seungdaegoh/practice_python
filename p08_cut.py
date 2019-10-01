#! /home/peter/anaconda3/bin/python3
#! /usr/bin/python3

import argparse
import os
import sys
import glob

parser = argparse.ArgumentParser(prog='cut.py', description='Print selected parts of lines from each FILE to standard output.' )
parser.add_argument('-d', '--delimiter' , metavar="DELIM", type=str,
		help='use DELIM instead of TAB for field delimiter')
parser.add_argument('-f', '--fields', metavar="LIST", type=str,
		help='select  only  these fields;  also print any line that contains no delimiter character, unless the -s option is specified')


args = parser.parse_args()
print('args.delimiter = [%s]' %(args.delimiter) )
print('typeof' , type( args.delimiter) )
d_str =  args.delimiter
if (len(d_str) != 1) :
	print( 'delimiter lenth error !! : Use only 1 charater')
	sys.exit(1)

print( 'delimiter str.len = ', len( d_str ), 'char = [%s]' %(d_str[0]) )
print( "args.fields = ", args.fields )

'''
# try 1
while True:
	line = input();
	if not line: break

	print(line)
'''

for line in sys.stdin:
	if ( "\n"  not in line ) :
		print ("xxx")
		break
	print(line, end = '')


	
'''

flist = args.files

for fname in flist:

    print("//----------- in file : ----------------- ", fname)

    f = open(fname, 'r')
    lines = f.readlines()

    nline = 1
    for line in lines:
        nline += 1

        if (line.find( key_word ) != -1): 
            print('line #', nline , ":", line, end = '')

    f.close()


'''
print('End of program')

