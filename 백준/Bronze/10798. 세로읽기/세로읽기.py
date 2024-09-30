import sys

S = []

for _ in range(5):
    S.append(sys.stdin.readline().rstrip())

for i in range(15):
    for j in range(5):
        if len(S[j]) <= i:
            continue
        print(S[j][i], end='')
