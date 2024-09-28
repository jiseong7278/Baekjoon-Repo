import sys

S = sys.stdin.readline().rstrip()

part = []

for i in range(len(S)):
    for j in range(len(S) - i):
        part.append(S[j:j+1+i])

print(len(set(part)))