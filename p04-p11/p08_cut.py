#! /usr/bin/python3
#! /home/peter/anaconda3/bin/python3

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

f_str =  args.fields

print( 'f_str = ' , f_str, 'f_str[0]-\'0\' = %d' %(ord(f_str[0]) - ord('0')))
st_i = ord(f_str[0]) - ord('0')
if (len(f_str) >= 2 and f_str[1] == '-') :
    ed_i = ord(f_str[2]) - ord('0')
else : 
    ed_i = st_i

print( 'st_i, ed_i = ', st_i, ed_i)

'''
# try 1
while True:
	line = input();
	if not line: break

	print(line)
'''

for line in sys.stdin:
    if ( "\n"  not in line ) :
    #print ("end of input")
        break

    #print(line, end = '')

    splited = line.split(d_str)

    idx = 0
    for stuff in splited :


        #print('stuff idx:', idx, '[', stuff, ']')
    
        if (idx >= st_i and idx <= ed_i) :
            print(stuff, end = ' ')

        idx += 1

    print('')
	
print('End of program')

