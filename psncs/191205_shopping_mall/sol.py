#!/usr/bin/env python3


import queue

N = 0
k = 0
data_wq = []
wq_i = 0
data_rq = []
tick_n = 0
out_seq = []

def find_empty(qi):
    if (data_rq[qi]):
        return False
    return True

def is_run_out(qi):
    v = data_rq[qi]
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
    v = data_wq[wq_i];
    wq_i += 1
    return v

def enq_run_q(qi, v):
    data_rq[qi] = v
    return

def deq_run_q(qi):
    v = data_rq[qi]
    data_rq[qi] = None
    return v

def tick(qi):
    v = data_rq[qi]
    v[1] -= 1


N, k = map(int, input().split())

print("N=", N, 'k=', k)

for i in range(N):
    _id, w = map(int, input().split())
    data_wq.append([_id, w])

for i in range(len(data_wq)):
    print(data_wq[i])

for i in range(k):
    data_rq.append([])


while (1):

    for rq_i in range(k):
        if (not find_empty(rq_i)):
            continue

        x = get_wait_q()
        enq_run_q(rq_i, x)


    while (1):
        tick_n += 1
        for rq_i in range(k):
            tick(rq_i)

        if (find_run_out()):
            break;


    for rq_i in range(k-1, -1, -1):
        if (find_empty(rq_i)):
            x = deq_run_q(rq_i)
            out_seq.append(x)

    break


print('-' * 15)
print(out_seq)





'''
#for i in range(k):
#    data_rq.append( queue.Queue() )

data_q[0].put(1)
data_q[0].put(2)
data_q[1].put(4)
data_q[1].put(3)

x = data_q[0].get()
print ("Q0 get=", x)

x = data_q[1].get()
print ("Q1 get=", x)
'''
