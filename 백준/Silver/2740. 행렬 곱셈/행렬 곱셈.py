def multi(a,b):
    X = [[0]*K for _ in range(N)]
    for i in range(N):
        for j in range(K):
            for k in range(M):
                X[i][j] += a[i][k]*b[k][j]
    return X

import sys
N, M = map(int, sys.stdin.readline().split())
A = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
M, K = map(int, sys.stdin.readline().split())
B = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
for i in multi(A,B):
    print(*i)