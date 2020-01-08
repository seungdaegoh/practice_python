#!/usr/bin/env python3

K =  int(input())
weights = list( map(int, input().split()))
#print("K=", K)
#print(weights)

sum_v = 0
run_wt = [0]

for i in weights:
    sum_v += i
    run_wt1 = [x + i for x in run_wt]
    run_wt2 = [x - i for x in run_wt]

    run_wt = list( set(run_wt + run_wt1 + run_wt2) )

    #print("new run_wt = ", run_wt)

run_wt.sort()


for i, w in enumerate(run_wt):
    if (w == 0):
        run_wt = run_wt[i + 1:]
        break

#print("run_wt = ", run_wt)

idx = 0
cnt = 0
for i in range(1, sum_v):


   if (i != run_wt[idx]):
       #print("Empty weight = ", i, "cmp_v=", run_wt[idx])
       cnt += 1
   else:
       idx += 1


print(cnt)

