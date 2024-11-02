import sys

C = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(2)]

A = C[0][0] * C[1][1] + C[1][0] * C[0][1]
B = C[0][1] * C[1][1]


def GCD(a, b):
    while b:
        a, b = b, a % b
    return a


gcd = GCD(A, B)

A = A // gcd
B = B // gcd

print(A, B)
