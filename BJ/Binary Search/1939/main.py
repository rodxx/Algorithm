import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, (input().split()))
g = [[] for _ in range(n+1)]
r = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))
start, end = map(int, input().split())
s, e = 1, 10**9

while s <= e:
    mid = (s+e)//2
    q = deque([start])
    v = [False]*(n+1)
    v[start] = True
    flag = 0

    while q:
        k = q.popleft()

        if k == end:
            flag = 1
            break

        for i in g[k]:
            if not v[i[0]] and i[1] >= mid:
                v[i[0]] = True
                q.append(i[0])
    if flag:
        s = mid+1
        r = mid
    else:
        e = mid-1
print(r)