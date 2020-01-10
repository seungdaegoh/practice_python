#!/usr/bin/env python3

nums = list( map(int, input().split()))

def compare_op(a, b, c):
    operators = ["+", "-", "*", "/"]
    for op in operators:
        if (op == "+"):
           left = a + b  
        elif (op == "-"):
           left = a - b  
        elif (op == "*"):
           left = a * b  
        elif (op == "/"):
           left = a // b  
        else:
           print("ERROR")

        if (left == c):
            return op
            break

    return None

op = compare_op(nums[0], nums[1], nums[2])

if (op):
    out_str = "{}{}{}={}".format(nums[0], op, nums[1], nums[2])
else:
    op = compare_op(nums[1], nums[2], nums[0])
    out_str = "{}={}{}{}".format(nums[0], nums[1], op, nums[2])
    
print(out_str)
