import sys
input = sys.stdin.readline

n = int(input())
dp = [[0]*10 for _ in range(n+1)]
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(2, n+1):
    for k in range(10):
        if k-1 >= 0:
            dp[i][k-1] += dp[i-1][k]
        if k+1 < 10:
            dp[i][k+1] += dp[i-1][k]
print(sum(dp[n]) % 10**9)