#!/usr/bin/env python3

M, N = tuple( map(int, input().split()))
#print("M=", M, "N=", N)
matrix = []

for i in range(M):
    matrix.append( list( map(int, input().split())))

nodes = []
node_sp = [0 for i in range(N)]

for i in range(N):
    nd_eg = []
    for j in range(N):

        if (i == j):
            continue

        if (matrix[0][i] >  matrix[0][j]):
            continue

        if (matrix[1][i] >  matrix[1][j]):
            continue

        if ( M == 2):
            nd_eg.append( j )
            node_sp[j] += 1

        elif (matrix[2][i] <  matrix[2][j]):
            nd_eg.append( j )
            node_sp[j] += 1

    nodes.append(nd_eg)
#print("after node_sp" , node_sp)

max_dep = 0


def dfs(pos, dep) :

    lenth = len(nodes[pos])

    global max_dep
    max_dep = max(dep, max_dep)

    for i in range(lenth):
        next_p = nodes[pos][i]
        dfs(next_p, dep + 1)



for i in range(N):
    if (node_sp[i] == 0):
        dfs(i, 1)

#print("max_dep=")
print(max_dep)
