import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
q = deque([n])
d = [-1]*100001
d[n] = 0

while q:
    p = q.popleft()

    if p == k:
        print(d[p])
        break

    dp = [-1, 1, p]
    for i in range(3):
        np = p + dp[i]
        if np < 0 or np > 100000:
            continue

        if d[np] < 0:
            d[np] = d[p] + 1
            q.append(np)