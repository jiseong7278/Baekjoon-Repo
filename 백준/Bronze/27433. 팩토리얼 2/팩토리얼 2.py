import sys

N = int(sys.stdin.readline().rstrip())

if N == 0:
    print(1)
else:
    answer = 1

    for i in range(1, N+1):
        answer *= i

    print(answer)