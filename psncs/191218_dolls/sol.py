#!/usr/bin/env python3

N, K = map(int, input().split())
nLike = list( map(int, input().split()))
#print("N K=", N, K)

var_tbl = [[-1 for col in range(N+1)] for row in range(N+1)]

def get_variance(st_i, ed_i):

    if (var_tbl[st_i][ed_i] != -1):
        print("------------- find tbl -------------")
        return var_tbl[st_i][ed_i]

    nCnt = (ed_i - st_i)
    #print("st_i, ed_i, cnt=", st_i, ed_i, nCnt)

    sum = 0
    for j in range(st_i, ed_i, 1):
#        print("[", nLike[j], "]", end='')
        sum += nLike[j]

    average = sum/ nCnt

    t_var = 0
    for j in range(st_i, ed_i, 1):
       t_var += (nLike[j] - average) ** 2

    var = t_var / nCnt

    var_tbl[st_i][ed_i] = var

#    print("\nVAR=", var, "\n")
    return var

   

min_var = -1
for k in range(K, N+1, 1):
    for i in range(N-k+1):
        #print("k=", k, "idx=", i)

        r_val = get_variance(i, i+k)

        if (min_var == -1 or min_var > r_val):
            min_var = r_val



#print("end_list")

print(min_var ** 0.5)




