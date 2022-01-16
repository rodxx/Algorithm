import sys
from collections import deque
input = sys.stdin.readline

def bfs(g, visit, v, p):
    queue = deque()
    queue.append(v)
    visit[v] = True
    while queue:
        k = queue.popleft()
        for i in g[k]:
            if not visit[i]:
                queue.append(i)
                visit[i] = True
                p[i] = k

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
parent = [0]*(n+1)

for _ in range(n-1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
bfs(graph, visited, 1, parent)

for i in parent[2:]:
    print(i)