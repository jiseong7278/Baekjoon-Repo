import sys

arr = []

for _ in range(int(sys.stdin.readline().rstrip())):
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort(reverse=True)

for i in range(len(arr)-2):
    if sum(arr[i+1:i+3]) > arr[i]:
        print(sum(arr[i:i+3]))
        break
else:
    print(-1)
