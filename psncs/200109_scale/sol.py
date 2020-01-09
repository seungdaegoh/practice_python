#!/usr/bin/env python3

K =  int(input())
weights = list( map(int, input().split()))

sum_v =  sum(weights)
run_wt = [0]

for i in weights:
    run_wt1 = [x + i for x in run_wt]
    run_wt2 = [x - i for x in run_wt]

    run_wt = list( set(run_wt + run_wt1 + run_wt2) )

run_wt.sort()

size_all = len( run_wt) // 2

cnt = sum_v - size_all
print(cnt)
