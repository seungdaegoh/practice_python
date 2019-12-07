#!/usr/bin/env python3

import queue

N = 0
k = 0
data_wq = []
wq_i = 0
data_rq = []
out_seq = []

def find_empty(qi):
    if (data_rq[qi]):
        return False
    return True

def is_run_out(qi):
    v = data_rq[qi]
    if (v == None):
        return False

    if (v[1] <= 0):
        return True
    return False

def find_run_out():
    for rq_i in range(k):
        if (is_run_out(rq_i)):
            return True
    return False

def get_wait_q():
    global wq_i
    if (wq_i >= N):
        return None

    v = data_wq[wq_i];
#    print("GET_WQ=", v)
    wq_i += 1
    return v

def enq_run_q(qi, v):
#    print("ENQ=", v)
    data_rq[qi] = v
    return

def deq_run_q(qi):
    v = data_rq[qi]
#    print("DEQ=", v)
    data_rq[qi] = None
    return v


def is_empty_all_rq():
    for rq_i in range(k):
        if (data_rq[rq_i] != None):
            return False
    return True


def tick(qi):
    v = data_rq[qi]
    if (v):
        v[1] -= 1


N, k = map(int, input().split())

for i in range(N):
    _id, w = map(int, input().split())
    data_wq.append([_id, w])

for i in range(k):
    data_rq.append([])

while (1):
    for rq_i in range(k):
        if (not find_empty(rq_i)):
            continue

        x = get_wait_q()
        if (not x):
            break
        enq_run_q(rq_i, x)

    while (1):
        for rq_i in range(k):
            tick(rq_i)

        if (find_run_out()):
            break;

    for rq_i in range(k-1, -1, -1):
        if (is_run_out(rq_i)):
            x = deq_run_q(rq_i)
            out_seq.append(x)

    if (is_empty_all_rq()):
        break

ans = 0
for idx, v in enumerate ( out_seq ):
    ans += ((idx + 1) * v[0])

print(ans)

