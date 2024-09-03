import sys

A, B = map(int, sys.stdin.readline().split())

cnt = 1
isPossible = False

while B > 1:
    if B % 2 == 0:
        B = B // 2
        cnt += 1
    elif B % 10 == 1:
        B = B // 10
        cnt += 1
    else:
        break

    if A == B:
        isPossible = True
        break

print(cnt if isPossible else -1)
