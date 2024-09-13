import sys

N = int(sys.stdin.readline().rstrip())

arr = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

arr.sort(key=lambda x: (x[1], x[0]))

for a in arr:
    print(a[0], a[1])