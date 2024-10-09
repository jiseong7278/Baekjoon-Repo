import sys

S = int(sys.stdin.readline().rstrip())

N = 0

while True:
    if S < N:
        N -= 1
        break
    S -= N
    N += 1

print(N)