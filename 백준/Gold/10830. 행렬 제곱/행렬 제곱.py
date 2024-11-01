import sys


def multi(a, b):
    x = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                x[i][j] += a[i][k] * b[k][j] % 1000
    return x


def square(a, n):
    if n == 1:
        return a
    else:
        temp = square(a, n // 2)
        if n % 2 == 0:
            return multi(temp, temp)
        else:
            return multi(multi(temp, temp), a)


N, B = map(int, sys.stdin.readline().rstrip().split())
A = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
result = square(A, B)
for i in range(N):
    for j in range(N):
        result[i][j] = result[i][j] % 1000

for r in result:
    print(*r)