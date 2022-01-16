import sys
from collections import deque
input = sys.stdin.readline

def bfs(g,v):
    queue = deque()
    visit = [False]*(n+1)

    visit[v] = True
    queue.append(v)
    while queue:
        k = queue.popleft()
        print(k,end=' ')
        for i in g[k]:
            if not visit[i]:
                visit[i] = True
                queue.append(i)

def dfs(g,v,visit):
    visit[v] = True
    print(v, end=' ')
    for i in g[v]:
        if not visit[i]:
            dfs(g,i,visit)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(n+1):
    graph[i] = sorted(graph[i])

dfs(graph, v, visited)
print()
bfs(graph, v)