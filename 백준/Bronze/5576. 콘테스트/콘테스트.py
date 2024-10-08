import sys

answer = []

for _ in range(2):

    arr = []

    for _ in range(10):
        arr.append(int(sys.stdin.readline().rstrip()))

    arr.sort()

    answer.append(sum(arr[7:]))

print(answer[0], answer[1])