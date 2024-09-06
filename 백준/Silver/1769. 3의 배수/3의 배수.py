import sys

N = sys.stdin.readline()

cnt = 0

N = N.replace('\n', "")

if int(N) > 9:
    while True:
        n_sum = 0
        cnt += 1
        for i in range(len(N)):
            n_sum += int(N[i])

        if n_sum < 10:
            break

        N = str(n_sum)

print(cnt)
print("YES" if int(N) % 3 == 0 else "NO")