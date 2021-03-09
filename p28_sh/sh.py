
import os
import sys
import subprocess


def run_cmd(exec_line):
    print( exec_line )
    #output = subprocess.run(exec_line,  stdout=subprocess.PIPE, shell=True)
    #output = subprocess.check_output(exec_line, shell=True, encoding='utf-8')
    out = subprocess.check_output(exec_line, shell=True, encoding='EUC-KR')
    print(out)


#print("argv", sys.argv)
#if (len(sys.argv)> 1):
#    run_cmd(sys.argv[1:])

while True:
    line = sys.stdin.readline()
    if (line == 'exit\n'):
        print("exit")
        break
    elif line == '':
        print("empty")
        break
    elif line == None:
        print("none")
        break

    elif line == '\n':
        continue

    cmd_ls = line.split()
    #print(cmd_ls)
    run_cmd(line)
