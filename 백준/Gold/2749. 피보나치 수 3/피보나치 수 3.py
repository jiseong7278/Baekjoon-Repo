import sys

N = int(sys.stdin.readline().rstrip())

a, b = 0, 1
N = N % (15 * (10**5))
for i in range(N):
    a, b = b % (10**6), (a+b) % (10**6)

print(a)