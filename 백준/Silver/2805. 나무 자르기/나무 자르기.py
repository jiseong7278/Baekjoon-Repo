import sys

K, N = map(int, sys.stdin.readline().rstrip().split())

wire = list(map(int, sys.stdin.readline().rstrip().split()))

start, end = 1, max(wire)

while start <= end:
    count = 0

    mid = (start + end) // 2

    for w in wire:
        if w > mid:
            count += w - mid

    if count < N:
        end = mid - 1
    else:
        start = mid + 1

print(end)