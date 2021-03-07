
import argparse
import os
import sys


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


def main(cmd, line, SET1, SET2=None):
    if ('simply' in cmd):
        simply = True
    else:
        simply = False

    if ('delete' in cmd):
        delete = True
    else:
        delete = False

    SET1a = get_append_str(SET1)
    print("SET1a=", SET1a)
    SET2a = None
    if (SET2):
        SET2a = get_append_str(SET2)
        print("SET2a=", SET2a)

    if (simply and delete):
        return "Error conflict command"

    if ((simply or delete) and SET2a):
        return "Error : no need SET2= " + SET2a + " str in this(-s, -d) flag"

    if (simply == False and delete == False):
        trans = True
    else:
        trans = False

    if (trans == True):
        if (SET2a == None):
            print("Error SET is None")
            return None
        if (len(SET1a) != len(SET2a)):
            print("Error SET1 and SET2 is different len")
            return None


    out_str = ''
    before_ch = None

    for i in range(len(line)):
        ch = line[i]

        if (simply and ch == before_ch and (ch in SET1a)):
            continue

        if (delete and (ch in SET1a)):
            continue

        if (trans and  (ch in SET1a)):
            idx = SET1a.index(ch)
            ch = SET2a[idx]

        out_str += ch
        before_ch = ch

    print("RESULT")
    print(out_str)
    return out_str


if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog='tr.py', description='translate' )
    parser.add_argument('-s', '--simply' , action="store_true")
    parser.add_argument('-d', '--delete', action="store_true")
    parser.add_argument('SET1',  type=str,  nargs='+' )

    args = parser.parse_args()
    cmd = []
    if (args.simply):
        cmd.append("simply")

    elif (args.delete):
        cmd.append("delete")

    '''
    print( args.simply)
    print( args.delete)
    print( args.SET1)
    '''


    SET1_str = args.SET1[0]
    print("args.SET1_str=", SET1_str)
    if (len(args.SET1) > 1):
        SET2_str = args.SET1[1]
        print("args.SET2_str=", SET2_str)

    lines =''
    while True:
        try:
            line = input() + "\n"
            # lines.append(line)
        except EOFError:
            break

    lines += line

    main (cmd, lines, SET1_str, SET2_str)