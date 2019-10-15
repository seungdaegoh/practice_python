#! /usr/bin/python3

import argparse
import os
import glob

parser = argparse.ArgumentParser(prog='grep', description='find a word in files' )
parser.add_argument('word',  type=str )
parser.add_argument('files',  type=str, nargs='+')


args = parser.parse_args()
key_word = args.word
#print( "args.word = ", args.word )
print( "key_word = ", key_word )
print( "args.files[0] = ", args.files[0] )

'''
print("getcwd() = ", os.getcwd() )

full_name =  os.getcwd() + '/' +  args.files[0] 
print("full_path ", full_name)

flist = glob.glob(full_name)
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


print('End of program')
