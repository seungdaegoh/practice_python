#!/usr/bin/env python3

x, y, c = map(float, input().split())


def get_proper(gv):

    a = (((x**2) - (gv**2)) **(1/2.0))
    b = (((y**2) - (gv**2)) **(1/2.0))
    A = c / a
    B = c / b
    K = A + B
#    print( "a=", a, "b=", b, "A=", A, "B=", B,  "K=", K)

    if (K > 0.9999999):
        return -1
    return 1

st = 0.0

if (x > y):
    ed = y
else :
    ed = x

while ((ed - st) > 0.000001):

    mid = (ed + st)/2
#    print("st:", st, "ed:", ed, "mid:", mid)

    if (get_proper(mid) < 0):
        ed = mid
    else :
        st = mid

#print("print ans = ")

print(st)




