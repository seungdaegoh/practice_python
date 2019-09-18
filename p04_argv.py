#!/usr/bin/python3


'''

import sys
param_n = len(sys.argv);

if  (param_n >= 2) :
	print(sys.argv[1]) 

if  (param_n >= 3) :
	print(sys.argv[2]) 

if  (param_n >= 4) :
	print(sys.argv[3]) 
'''




import argparse
parser = argparse.ArgumentParser()


parser.add_argument("-v", "--verbosity", help="increase output verbosity",
                            action="count")

parser.add_argument('--op', type=str, default='add',
                    choices=['add','sub','mul','div'],
                                help='What operation?')

parser.add_argument("left", type=int, help="input l-value which will be used by operation")
parser.add_argument("right", type=int, help="input r-value which will be used by operation")



args = parser.parse_args()


'''
if args.verbosity == 1:
    print("{}^2 == {}".format(args.square, answer))
elif args.verbosity == 2:
    print("the square of {} equals {}".format(args.square, answer))
else:
    print("Ans: ", answer)

#print(args.square**2)
'''

lv = args.left
rv = args.right
op = args.op

if op == 'add' :
    ans = lv + rv

elif op == 'sub' :
    ans = lv - rv

elif op == 'mul' :
    ans = lv * rv

elif op == 'div' :
    ans = lv / rv

print("Answer = ", ans)
print("End of Program")

