import sys

A, B, C = map(int, sys.stdin.readline().rstrip().split())


def multiply(a, n):
    if n == 1:
        return a % C
    else:
        temp = multiply(a, n // 2)
        if n % 2 == 0:
            return temp * temp % C
        else:
            return temp * temp * a % C

print(multiply(A, B))