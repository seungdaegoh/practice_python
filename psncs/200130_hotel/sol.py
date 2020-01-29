#!/usr/bin/env python3

T =  int(input())

for i in range(T):
    H, W, N = tuple( map(int, input().split()))
    h = ((N-1) % H) + 1
    w = (((N - 1) // H) + 1) % 100
    print(h, end='')
    print("{0:02d}".format(w))

#print("End")
