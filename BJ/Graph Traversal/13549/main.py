import sys
from collections import deque

input = sys.stdin.readline


def bfs(s):
    queue = deque([s])
    d[s] = 0
    while queue:
        n = queue.popleft()
        r = [-1, 1, n]

        for i in range(3):
            pn = n + r[i]
            if 0 > pn or pn > 100000:
                continue

            cost = d[n]
            if i < 2:
                cost += 1

            if d[pn] < 0:
                queue.append(pn)
                d[pn] = cost
            elif cost < d[pn]:
                d[pn] = cost


num, k = map(int, input().split())
d = [-1] * 100001

bfs(num)
print(d[k])