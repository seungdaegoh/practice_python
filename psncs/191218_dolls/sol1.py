#!/usr/bin/env python3

N, K = map(int, input().split())
nLike = list( map(int, input().split()))

def get_variance(st_i, ed_i):

    nCnt = (ed_i - st_i)

    sum = 0
    for j in range(st_i, ed_i, 1):
        sum += nLike[j]

    average = sum/ nCnt

    t_var = 0
    for j in range(st_i, ed_i, 1):
       t_var += (nLike[j] - average) ** 2

    var = t_var / nCnt
    return var

   
min_var = -1
for k in range(K, N+1, 1):
    for i in range(N-k+1):
	
        r_val = get_variance(i, i+k)

        if (min_var == -1 or min_var > r_val):
            min_var = r_val

print(min_var ** 0.5)




