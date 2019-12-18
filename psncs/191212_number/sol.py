#!/usr/bin/env python3

MAX_S = 10000000

N = int(input())

card = list( map(int, input().split()))

M = int(input())
num = list( map(int, input().split()))


array = [0]*(2 * MAX_S )

for i in range(N):
    array[ card[i] - MAX_S] = 1

for i in range(M):
    if (array[ num[i] - MAX_S] > 0):
        print(1, end=' ')
    else:
        print(0, end=' ')

print(" ")

