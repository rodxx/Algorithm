import sys
from itertools import accumulate
n = int(sys.stdin.readline().rstrip())
honey = list(map(int, sys.stdin.readline().rstrip().split()))
dp = list(accumulate(honey)) ; result = 0
for start2 in range(1, n-1):
  result1 = (dp[start2] - dp[0]) + (dp[n-2] - dp[start2 - 1])
  result2 = dp[start2 - 1] + dp[n-2] - honey[start2]
  result3 = (dp[n-1] - dp[0]) + (dp[n-1] - dp[start2]) - honey[start2]
  result = max(result, result1, result2, result3)
print(result)