import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

arr = []

for i in range(1, N+1):
    if N % i == 0:
        arr.append(i)

if K <= len(arr):
    print(arr[K-1])
else:
    print(0)