
import argparse
import os
import sys

parser = argparse.ArgumentParser(prog='tr.py', description='translate' )
parser.add_argument('-s', '--simply' , action="store_true")
parser.add_argument('-d', '--delete', action="store_true")
parser.add_argument('SET1',  type=str,  nargs='+' )

args = parser.parse_args()
'''
print( args.simply)
print( args.delete)
print( args.SET1)
'''


def get_append_str(in_word):
    ch_list = ''
    ch_to_next = False

    for i in range(len(in_word)):
        ch = in_word[i]
        if (ch == '-'):
            ch_to_next = True
        elif (ch_to_next):
            ed_ch = ch
            while (now_ch != ed_ch):
                now_ch = chr(ord(now_ch) + 1)
                ch_list += now_ch

            ch_to_next = False

        else:
            to_next = False
            ch_list += ch
            now_ch = ch
            ch_to_next = False

    return ch_list

SET1_str = get_append_str(args.SET1[0])
print("SET1_str=", SET1_str)
if (len(args.SET1) > 1):
    SET2_str = get_append_str(args.SET1[1])
    print("SET1_str=", SET2_str)


in_method = sys.stdin
for line in in_method:
    if ( "\n"  not in line ) :
        print ("____end of input___")
        break

    out_str = ''
    before_ch = None
    for i in range(len(line)):
        ch = line[i]

        if (args.simply):

            if (ch == before_ch  and (ch in SET1_str)):
                continue

        out_str += ch

        before_ch = ch


    print("RESULT")
    print(out_str)