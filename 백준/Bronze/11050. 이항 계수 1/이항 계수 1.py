import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

dp = [1, 1, 2]

if n > 2:
    for i in range(3, n+1):
        dp.append(dp[i - 1] * i)

print(dp[n]//(dp[n-k]*dp[k]))