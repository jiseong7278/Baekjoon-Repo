import sys

answer = 0

for _ in range(5):
    n = int(sys.stdin.readline().strip())

    if n < 40:
        answer += 40
    else:
        answer += n

print(answer // 5)