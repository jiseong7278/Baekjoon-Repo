import sys

n = int(sys.stdin.readline().rstrip())

arr = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

x = int(sys.stdin.readline().rstrip())

start, end = 0, len(arr)-1

answer = 0

while start < end:
    if arr[start] + arr[end] == x:
        answer += 1
        start += 1
        end -= 1
    elif arr[start] + arr[end] < x:
        start += 1
    elif arr[start] + arr[end] > x:
        end -= 1

print(answer)