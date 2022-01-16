import sys
from collections import deque
input = sys.stdin.readline

def bfs(g, v):
    queue = deque()
    visit = [False]*(n+1)

    queue.append(v)
    visit[v] = True
    cnt = 0
    while queue:
        k = queue.popleft()
        for i in g[k]:
            if not visit[i]:
                queue.append(i)
                visit[i] = True
                cnt += 1
    return cnt

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
hack = []
for _ in range(m):
    s, e = map(int, input().split())
    graph[e].append(s)

max_c = -1
for i in range(1,n+1):
    c = bfs(graph,i)
    if max_c == c:
        hack.append(i)
    elif max_c < c:
        max_c = c
        hack.clear()
        hack.append(i)

for i in hack:
    print(i, end=' ')